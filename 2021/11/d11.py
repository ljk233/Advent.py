
# 2021, Day 10: Syntax Scoring
# %timeit = 71.9 ms ± 179 µs


# %%
from collections import namedtuple
from typing import NamedTuple
import numpy as np
from numpy.typing import NDArray


sol = namedtuple('Solution', ['part1', 'part2'])

# **************
# Infrastructure
# **************

def indices(arr: NDArray):
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            yield (i, j)


def neighbours(arr: NDArray, idx: tuple[int, int]) -> list[tuple[int, int]]:
    m, n = arr.shape
    for i in range(-1, 2):
        for j in range(-1, 2):
            nxt = (idx[0]+i, idx[1]+j)
            if nxt != idx and nxt[0] in range(0, m) and nxt[1] in range(0, n):
                yield nxt


def make_cavern(input: list[str]) -> NDArray:
    m, n = len(input), len(input[0])
    cavern = np.zeros((m, n), dtype=int)
    for i in range(m):
        for j in range(n):
            cavern[i, j] = int(input[i][j])
    return cavern


# ********
# Solution
# ********


def tick(cavern: NDArray) -> int:
    cavern += 1
    flashed = set()
    ready = set([idx for idx in indices(cavern) if cavern[idx] > 9])

    while len(ready) >= 1:
        flashing = ready.pop()
        flashed.add(flashing)
        for idx in neighbours(cavern, flashing):
            cavern[idx] += 1
            if cavern[idx] > 9 and idx not in flashed:
                ready.add(idx)

    for idx in flashed:
        cavern[idx] = 0

    return len(flashed)


def solve(f: str) -> NamedTuple:
    with open(f, "r") as f:
        input: list[str] = f.read().splitlines()
    cavern = make_cavern(input)

    k = 0
    flashed100 = 0
    still_synching = True
    while still_synching:
        k += 1
        flashed = tick(cavern)
        if k <= 100:
            flashed100 += flashed
        still_synching = flashed != cavern.size

    return sol(flashed100, k)


print("SAMPLE: ", solve("sample.txt"))
print("INPUT:  ", solve("input.txt"))

# %%
