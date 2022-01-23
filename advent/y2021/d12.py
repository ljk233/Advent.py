

from ..solution import Solution
from collections import namedtuple, defaultdict


def get_paths(input: list[str]) -> defaultdict[str, list[str]]:
    paths: defaultdict[str, list[str]] = defaultdict(list)
    for line in input:
        st, en = line.split("-")
        if st != "start":
            paths[en].append(st)
        if en != "start":
            paths[st].append(en)
    return paths


def is_small(cave: str) -> bool:
    return cave[0].islower()


def have_visited(cave, visited) -> bool:
    return visited[cave] >= 1


# backtracking recursive function
def search(visited, caves, cave, can_revisit):
    if have_visited(cave, visited) and not can_revisit:
        return 0
    elif cave == "end":
        return 1
    else:
        if is_small(cave):
            visited[cave] += 1
        proc = can_revisit and visited[cave] <= 1
        paths = [search(visited, caves, next, proc) for next in caves[cave]]
        if is_small(cave):
            visited[cave] -= 1
        return sum(paths)


def solve(input: list[str]) -> Solution:
    # for defaultdict
    def zero():
        return 0
    paths = get_paths(input)
    visited = defaultdict(zero)
    return Solution(
        search(visited, paths, "start", False),
        search(visited, paths, "start", True)
    )
