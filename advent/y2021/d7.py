
from ..solution import Solution
from math import ceil, floor
from statistics import median, mean


def cost(crabs_pos: list[int], mean_pos: int) -> int:
    fuel = [abs(pos - mean_pos) for pos in crabs_pos]
    adj = []
    while len(fuel) >= 1:
        adj.append(sum(x for x in range(1, fuel.pop()+1)))
    return sum(adj)


def solve(input: list[str]) -> Solution:
    crabs_pos = sorted([int(x) for x in input[0].split(",")])
    mean_pos = mean(crabs_pos)  # save us calculating the mean position twice
    return Solution(
        sum([abs(pos - int(median(crabs_pos))) for pos in crabs_pos]),
        min(cost(crabs_pos, floor(mean_pos)), cost(crabs_pos, ceil(mean_pos))),
    )
