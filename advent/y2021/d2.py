
from ..solution import Solution
from dataclasses import dataclass
from typing import NoReturn


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
class AimSubmarine(Submarine):
    aim: int = 0

    def next(self, cmd: str, step: int) -> NoReturn:
        if cmd == "up":
            self.aim -= step
        elif cmd == "down":
            self.aim += step 
        else:
            self.x += step
            self.y += (self.aim * step)


def solve(input: list[str]) -> Solution:
    sub = Submarine()
    aimsub = AimSubmarine()
    for line in input:
        cmd, step = line.split()
        sub.next(cmd, int(step))
        aimsub.next(cmd, int(step))
    return Solution(sub.x * sub.y, aimsub.x * aimsub.y)
