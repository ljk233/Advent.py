
from ..solution import Solution
from collections import defaultdict


def get_paths(input: list[str]) -> defaultdict[str, list[str]]:
    paths: defaultdict[str, list[str]] = defaultdict(list)
    for line in input:
        st, en = line.split("-")
        if st != "start":
            paths[en].append(st)
        if en != "start":
            paths[st].append(en)
    return paths


def has(visited, cave) -> bool:
    return visited[cave] >= 1


def is_small(cave: str) -> bool:
    return cave[0].islower()


def search(caves, cave, visited, can_revisit):
    if has(visited, cave) and not can_revisit:
        return 0
    elif cave == "end":
        return 1
    else:
        if is_small(cave):
            visited[cave] += 1
        can_proceed = can_revisit and visited[cave] <= 1
        subtotal = 0
        for next_cave in caves[cave]:
            subtotal += search(caves, next_cave, visited, can_proceed)
        if is_small(cave):
            visited[cave] -= 1
        return subtotal


def solve(input: list[str]) -> Solution:
    # for defaultdict
    def zero():
        return 0
    paths = get_paths(input)
    visited = defaultdict(zero)
    return Solution(
        search(paths, "start", visited, can_revisit=False),
        search(paths, "start", visited, can_revisit=True)
    )
