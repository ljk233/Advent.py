
# 2021, Day 2: Dive!
# %timeit = 769 µs ± 2.43 µs

# %%
from collections import namedtuple
from dataclasses import dataclass
from typing import NoReturn


sol = namedtuple('Solution', ['part1', 'part2'])


@dataclass
class Submarine:
    x: int = 0
    y: int = 0

    def next(self, cmd: str, step: int) -> NoReturn:
        if cmd == "up":
            self.y -= step
        elif cmd == "down":
            self.y += step 
        else:
            self.x += step


@dataclass
class AimSubmarine:
    x: int = 0
    y: int = 0
    aim: int = 0

    def next(self, cmd: str, step: int) -> NoReturn:
        if cmd == "up":
            self.aim -= step
        elif cmd == "down":
            self.aim += step 
        else:
            self.x += step
            self.y += (self.aim * step)


def solve(f: str):
    with open(f, "r") as f:
        input: list[str] = f.read().splitlines()
    sub = Submarine()
    aimsub = AimSubmarine()
    for line in input:
        cmd, step = line.split()
        sub.next(cmd, int(step))
        aimsub.next(cmd, int(step))

    return sol(sub.x * sub.y, aimsub.x * aimsub.y)


print("SAMPLE: ", solve("sample.txt"))
print("INPUT:  ", solve("input.txt"))
