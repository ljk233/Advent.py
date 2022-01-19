
# 2021, Day 10: Syntax Scoring
# %timeit = 1.51 ms ± 8.43 µs

# %%
from collections import namedtuple
from typing import NamedTuple
from statistics import median


sol = namedtuple('Solution', ['part1', 'part2'])


def score(line: str) -> tuple[str, int]:
    brackets = {")": "(", "]": "[", "}": "{", ">": "<"}
    corr_score = {")": 3, "]": 57, "}": 1197, ">": 25137}

    left = []  # a stack
    # check if corrupted
    for bracket in line:
        if bracket in brackets.values():
            left.append(bracket)
        elif len(left) >= 1 and brackets[bracket] == left[-1]:
            left.pop()
        elif len(left) >= 1 and brackets[bracket] != left[-1]:
            return "corrupted", corr_score[bracket]

    # autocompletion needed
    auto_score = {"(": 1, "[": 2, "{": 3, "<": 4}
    score = 0
    while len(left) >= 1:
        score *= 5
        score += auto_score[left.pop()]
    return "autocomplete", score              


def solve(f: str) -> NamedTuple:
    with open(f, "r") as f:
        input: list[str] = f.read().splitlines()

    corr_score = 0
    auto_scores = []
    for line in input:
        res = score(line)
        if res[0] == "corrupted":
            corr_score += res[1]
        else:
            auto_scores.append(res[1])

    return sol(
        corr_score,
        int(median(sorted(auto_scores)))
    )


print("SAMPLE: ", solve("sample.txt"))
print("INPUT:  ", solve("input.txt"))

# %%
