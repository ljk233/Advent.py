
from ..solution import Solution
from collections import  deque
from typing import NoReturn


def simulate(lantern_fish: deque[int]) -> NoReturn:
    lantern_fish.append(lantern_fish.popleft())
    lantern_fish[6] += lantern_fish[-1]


def solve(input: list[str]) -> Solution:
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
    
    return Solution(sum80, sum256)
