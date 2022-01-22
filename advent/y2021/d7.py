
from ..solution import Solution
from math import ceil, floor
from statistics import median, mean


def abs_diff(a, b) -> int:
    return int(abs(a - b))


def sum_to(n: int) -> int:
    return int((n * (n + 1)) / 2)


def median_cost(crabs_pos) -> int:
    med_pos = int(median(crabs_pos))
    return sum([abs_diff(pos, med_pos) for pos in crabs_pos])


def mean_cost(crabs_pos) -> int:
    mean_pos = mean(crabs_pos)
    return  min(
        sum([sum_to(abs_diff(pos, floor(mean_pos))) for pos in crabs_pos]),
        sum([sum_to(abs_diff(pos, ceil(mean_pos))) for pos in crabs_pos])
    )


def solve(input: list[str]) -> Solution:
    crabs_pos = sorted([int(x) for x in input[0].split(",")])
    return Solution(median_cost(crabs_pos), mean_cost(crabs_pos))
