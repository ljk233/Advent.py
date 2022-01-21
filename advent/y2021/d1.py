
from ..solution import Solution


def diff(depths: list[int], width: int) -> int:
    increased = 0
    for idx in range(len(depths)-width):
        if depths[idx+width] - depths[idx] > 0:
            increased += 1
    return increased


def solve(input: list[str]) -> Solution:
    depths = [int(line) for line in input]
    return Solution(diff(depths, 1), diff(depths, 3))
