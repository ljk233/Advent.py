
# 2021, Day 9: Smoke Basin
# %timeit: 30.1 ms ± 650 µs


# %%
from collections import namedtuple
from typing import NamedTuple
import numpy as np
from numpy.typing import NDArray
from math import prod


sol = namedtuple('Solution', ['part1', 'part2'])


def height_map(input: list[str]) -> NDArray:
    arr = np.array([int(line[x]) for line in input for x in range(len(line))])
    return arr.reshape(len(input), len(input[1]))


def indices(hmap: NDArray):
    for i in range(hmap.shape[0]):
        for j in range(hmap.shape[1]):
            yield (i, j)


def neighbours(idx: tuple[int, int]) -> list[tuple[int, int]]:
    x, y = idx
    return [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]


def in_bounds(hmap: NDArray, idx: tuple[int, int]) -> bool:
    x, y = idx
    m, n = hmap.shape
    return x >= 0 and x < m and y >= 0 and y < n


def is_low_point(hmap: NDArray, pos: tuple[int, int], visited: set[tuple[int, int]]) -> bool:
    is_low = True
    for neighbour in neighbours(pos):
        if in_bounds(hmap, neighbour):
            if hmap[neighbour] > hmap[pos]:
                visited.add(neighbour)
            else:
                is_low = False
    return is_low


def low_points(hmap: NDArray) -> list[tuple[int, int]]:
    visited = set()
    lows = []
    for idx in indices(hmap):
        if idx not in visited:
            visited.add(idx)
            if is_low_point(hmap, idx, visited):
                lows.append(idx)

    return lows


def basin_sizes(hmap: NDArray, lows: list[tuple[int, int]]):
    # recursive depth-first search
    def dfs(hmap, visited: set[tuple[int, int]], pos: tuple[int, int]):
        if pos in visited or hmap[pos] == 9:
            return 0
        size = 1
        for neighbour in neighbours(pos):
            if in_bounds(hmap, neighbour):
                visited.add(pos)
                size += dfs(hmap, visited, neighbour)
        return size

    sizes = []
    visited = set()
    for low in lows:
        sizes.append(dfs(hmap, visited, low))
    return sizes


def solve(f: str) -> NamedTuple:
    with open(f, "r") as f:
        input: list[str] = f.read().splitlines()

    hmap = height_map(input)
    lows = low_points(hmap)
    top3_sizes = sorted(basin_sizes(hmap, lows), reverse=True)[0:3]

    return sol(
        sum([1 + hmap[x] for x in lows]),
        prod([size for size in top3_sizes]),
    )


print("SAMPLE: ", solve("sample.txt"))
print("INPUT:  ", solve("input.txt"))
