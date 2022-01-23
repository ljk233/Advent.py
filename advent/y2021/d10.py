
from ..solution import Solution
from statistics import median
from dataclasses import dataclass


BRACKETS: dict[str, str] = {")": "(", "]": "[", "}": "{", ">": "<"}
CORRUPTED_SCORE: dict[str, int] = {")": 3, "]": 57, "}": 1197, ">": 25137}
AUTOCOMP_SCORE : dict[str, int] = {"(": 1, "[": 2, "{": 3, "<": 4}


@dataclass
class LineScore:
    type: str
    score: int
    def is_corrupted(self) -> bool:
        return self.type == "corrupted"


def score(line: str) -> LineScore:
    open = []  # stack
    for bracket in line:
        if bracket in BRACKETS.values():
            open.append(bracket)
        elif len(open) >= 1 and BRACKETS[bracket] == open[-1]:
            open.pop()
        elif len(open) >= 1 and BRACKETS[bracket] != open[-1]:
            return LineScore("corrupted", CORRUPTED_SCORE[bracket])

    # autocompletion needed
    score = 0
    while len(open) >= 1:
        score *= 5
        score += AUTOCOMP_SCORE[open.pop()]
    return LineScore("autocompleted", score) 


def solve(input: list[str]) -> Solution:
    corr_score = 0
    auto_scores = []
    for line in input:
        res = score(line)
        if res.is_corrupted():
            corr_score += res.score
        else:
            auto_scores.append(res.score)

    return Solution(
        corr_score,
        int(median(sorted(auto_scores)))
    )
