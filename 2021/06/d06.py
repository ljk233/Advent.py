
# 2021, Day 6: Lanternfish
# @Benchmark: 189 µs ± 552 ns


# %%
from collections import namedtuple, deque
from typing import NamedTuple, NoReturn


sol = namedtuple('Solution', ['part1', 'part2'])


def simulate(lantern_fish: deque[int]) -> NoReturn:
    lantern_fish.append(lantern_fish.popleft())
    lantern_fish[6] += lantern_fish[-1]


def solve(f: str) -> NamedTuple:
    with open(f, "r") as f:
        input: list[str] = f.read().splitlines()
    numbers = [int(x) for x in input[0].split(",")]
    lantern_fish = deque([numbers.count(number) for number in range(9)])
    # part 1, 80 days
    for _ in range(80):
        simulate(lantern_fish)
    sum80 = sum(lantern_fish)
    # part 2, 256 day
    for _ in range(176):
        simulate(lantern_fish)
    sum256 = sum(lantern_fish)
    
    return sol(sum80, sum256)


#%%
print("SAMPLE: ", solve("sample.txt"))
print("INPUT:  ", solve("input.txt"))
