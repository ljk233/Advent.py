
from ..solution import Solution
from collections import  Counter
from dataclasses import dataclass
from parse import parse
from typing import NoReturn


@dataclass
class Point:
    x: int = 0
    y: int = 0


def get_endpoints(line: str) -> tuple[Point, Point]:
    res = parse("{x1:d},{y1:d} -> {x2:d},{y2:d}", line)
    if res["x1"] <= res["x2"]:
        return Point(res["x1"], res["y1"]), Point(res["x2"], res["y2"])
    else:
        return Point(res["x2"], res["y2"]), Point(res["x1"], res["y1"])


def yrange(a: Point, b: Point) -> list[int]:
    if a.y < b.y:
        return [y for y in range(a.y, (b.y + 1))]
    else:
        return [y for y in range(a.y, (b.y - 1), -1)]


def is_diagonal(a, b) -> bool:
    return (a.x != b.x) and (abs((a.y - b.y)/(a.x - b.x)) == 1)


def count_points(counters, a: Point, b: Point) -> NoReturn:
    if is_diagonal(a, b):
        dx = 0
        for y in yrange(a, b):
            counters[1][(a.x+dx, y)] += 1
            dx += 1
    elif a.x == b.x:
        for y in yrange(a, b):
            counters[0][(a.x, y)] += 1
            counters[1][(a.x, y)] += 1
    elif a.y == b.y:
        for x in range(a.x, (b.x + 1)):
            counters[0][(x, a.y)] += 1
            counters[1][(x, a.y)] += 1


def intersections(counter: Counter) -> int:
    return sum([val >= 2 for val in counter.values()])


def solve(input: list[str]) -> Solution:
    counters = (Counter(), Counter())
    for line in input:
        a, b = get_endpoints(line)
        count_points(counters, a, b)
    return Solution(intersections(counters[0]), intersections(counters[1]))
