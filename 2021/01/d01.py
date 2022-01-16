
# %%
from collections import namedtuple
from typing import NamedTuple


sol = namedtuple('Solution', ['part1', 'part2'])


def diff(depths: list[int], width: int) -> int:
    increased = 0
    for idx in range(0, len(depths)-width):
        if depths[idx+width] - depths[idx] > 0:
            increased += 1
    return increased


def solve(f: str) -> NamedTuple:
    with open(f, "r") as f:
        input = f.read().splitlines()
    depths = [int(line) for line in input]
    return sol(diff(depths, 1), diff(depths, 3),)


print("SAMPLE: ", solve("sample.txt"))
print("INPUT:  ", solve("input.txt"))
