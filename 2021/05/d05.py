
# 2021, Day 5: Hydrothermal Venture
# %timeit: 160 ms ± 1.47 ms


# %%
from collections import namedtuple, Counter
from dataclasses import dataclass
from typing import NamedTuple
from parse import parse


sol = namedtuple('Solution', ['part1', 'part2'])


@dataclass
class Point:
    x: int = 0
    y: int = 0


def get_ab(line: str) -> tuple[Point, Point]:
    res = parse("{x1:d},{y1:d} -> {x2:d},{y2:d}", line)
    if res["x1"] <= res["x2"]:
        return Point(res["x1"], res["y1"]), Point(res["x2"], res["y2"])
    else:
        return Point(res["x2"], res["y2"]), Point(res["x1"], res["y1"])


def range_y(a, b) -> list[int]:
    if a.y < b.y:
        return [y for y in range(a.y, (b.y + 1))]
    else:
        return [y for y in range(a.y, (b.y - 1), -1)]


def is_diagonal(a, b) -> bool:
    return (a.x != b.x) and (abs((a.y - b.y)/(a.x - b.x)) == 1)


def mark(counters, line: str):
    a, b = get_ab(line)
    if is_diagonal(a, b):
        dx = 0
        for y in range_y(a, b):
            counters[1][(a.x+dx, y)] += 1
            dx += 1
    elif a.x == b.x:
        for y in range_y(a, b):
            counters[0][(a.x, y)] += 1
            counters[1][(a.x, y)] += 1
    elif a.y == b.y:
        for x in range(a.x, (b.x + 1)):
            counters[0][(x, a.y)] += 1
            counters[1][(x, a.y)] += 1
    return counters


def intersections(counter: Counter) -> int:
    n = 0
    for val in counter.values():
        if val >= 2:
            n += 1
    return n


def solve(f: str) -> NamedTuple:
    with open(f, "r") as f:
        input: list[str] = f.read().splitlines()
    counters = (Counter(), Counter())
    for line in input:
        mark(counters, line)
    return sol(intersections(counters[0]), intersections(counters[1]))


print("SAMPLE: ", solve("sample.txt"))
print("INPUT:  ", solve("input.txt"))
