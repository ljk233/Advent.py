
from ..solution import Solution
from ..mat import are_diag, as_matrix, each_index, each_neighbour, CartesianIndex
from math import prod
from numpy.typing import NDArray


def is_low(hmap: NDArray, index: CartesianIndex, visited: set[CartesianIndex]) -> bool:
    is_low = True
    for neighbour in each_neighbour(hmap, index):
        if hmap[neighbour] > hmap[index]:
            # neighbour cannot be a low point, so do not revisit
            visited.add(neighbour)
        else:
            is_low = False

    return is_low


def find_low_points(hmap: NDArray) -> list[CartesianIndex]:
    """Return a list of local low points in the given hmap.
    """
    visited = set()
    lows = []
    for index in each_index(hmap):
        if index not in visited:
            visited.add(index)
            if is_low(hmap, index, visited):
                lows.append(index)

    return lows


def risk_levels(hmap: NDArray, low_points) -> list[int]:
    return [1 + hmap[low_point] for low_point in low_points]


def search(hmap, visited, pos) -> int:
    if hmap[pos] == 9:
        return 0
    size = 1
    visited.add(pos)
    for neighbour in each_neighbour(hmap, pos):
        if neighbour not in visited and not are_diag(neighbour, pos):
            size += search(hmap, visited, neighbour)

    return size


def basin_sizes(hmap: NDArray, low_points: list) -> list[int]:
    sizes = []
    visited = set()
    for low in low_points:
        sizes.append(search(hmap, visited, low))
    return sizes


def solve(input: list[str]) -> Solution:
    hmap = as_matrix(input)
    low_points = find_low_points(hmap)
    top3_basin_sizes = sorted(basin_sizes(hmap, low_points), reverse=True)[:3]

    return Solution(
        sum(risk_levels(hmap, low_points)),
        prod(top3_basin_sizes)
    )
