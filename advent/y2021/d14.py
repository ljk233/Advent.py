
from ..solution import Solution
from collections import Counter
from parse import parse


def get_template(input: str) -> Counter[str]:
    temp = Counter([input[i] + input[i+1] for i in range(len(input)-1)])
    temp[input[0][-1] + "_"] += 1
    return temp


def get_rules(input: list[str]) -> dict[str, str]:
    rules = {}
    for line in input[2:]:
        m = parse("{left} -> {right}", line)
        rules[m['left']] = m['right']
    return rules


def extend_polymer(polymer: Counter[str], rules: dict[str, str]) -> Counter[str]:
    extended_polymer = Counter()
    for (pair, occ) in polymer.items():
        if pair in rules:
            extended_polymer[pair[0] + rules[pair]] += occ
            extended_polymer[rules[pair] + pair[1]] += occ
        else:
            extended_polymer[pair] = occ
    return extended_polymer


def diff_min_max(polymer: Counter[str]) -> int:
    k_elements = Counter()
    for (pair, occ) in polymer.items():
        k_elements[pair[0]] += occ
    occs = sorted(k_elements.values())
    return occs[-1] - occs[0]


def solve(input: list[str]) -> Solution:
    polymer = get_template(input[0])
    rules = get_rules(input)

    for _ in range(10):
        polymer = extend_polymer(polymer, rules)
    diff10 = diff_min_max(polymer)

    for _ in range(30):
        polymer = extend_polymer(polymer, rules)
    diff40 = diff_min_max(polymer)

    return Solution(diff10, diff40)
