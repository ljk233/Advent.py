
# 2021, Day 7: The Treachery of Whales
# @Benchmark: 35.1 ms ± 109 µs


# %%
from collections import namedtuple, deque
from math import ceil, floor
from statistics import median, mean
from typing import NamedTuple, NoReturn


sol = namedtuple('Solution', ['part1', 'part2'])


def cost(crabs_pos, mean_pos):
    fuel = [abs(pos - mean_pos) for pos in crabs_pos]
    adj = []
    while len(fuel) >= 1:
        adj.append(sum(x for x in range(1, fuel.pop()+1)))
    return sum(adj)


def solve(f: str) -> NamedTuple:
    with open(f, "r") as f:
        input: list[str] = f.read().splitlines()
    crabs_pos = sorted([int(x) for x in input[0].split(",")])
    mean_pos = mean(crabs_pos)  # save us calculating the mean position twice
    return sol(
        sum([abs(pos - int(median(crabs_pos))) for pos in crabs_pos]),
        min(cost(crabs_pos, floor(mean_pos)), cost(crabs_pos, ceil(mean_pos))),
    )


solve("sample.txt")


#%%
print("SAMPLE: ", solve("sample.txt"))
print("INPUT:  ", solve("input.txt"))
