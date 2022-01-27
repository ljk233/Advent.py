
from ..mat import each_index
from parse import parse
import numpy as np
from numpy.typing import NDArray


def is_up_fold(fold: tuple[str, int]) -> bool:
    return fold[0] == 'y'


def get_dots(input: list[str]) -> set[tuple[int, int]]:
    dots = set()
    for index in range(input.index('')):
        m = parse("{x:d},{y:d}", input[index])
        dots.add((m['x'], m['y']))
    return dots


def get_folds(input) -> list[tuple[int, int]]:
    folds = []
    for index in range(len(input)-1, input.index(''), -1):
        m = parse("fold along {axis}={pos:d}", input[index])
        folds.append((m['axis'], m['pos']))
    return folds


def do_fold(fold: tuple[int, int], dots: set[tuple[int, int]]) -> set[tuple[int, int]]:
    new_dots = set()
    for dot in dots:
        if is_up_fold(fold) and fold[1] < dot[1]:
            new_dots.add((dot[0], 2*fold[1] - dot[1]))
        elif not is_up_fold(fold) and fold[1] < dot[0]:
            new_dots.add((2*fold[1] - dot[0], dot[1]))
        else:
            new_dots.add(dot)
    return new_dots


def get_shape(dots) -> tuple[int, int]:
    m, n = 0, 0
    for dot in dots:
        if dot[0] > m:
            m = dot[0]
        if dot[1] > n:
            n = dot[1]
    return m, n


def make_paper(dots):
    m, n = get_shape(dots)
    paper = np.zeros((m+1, n+1), dtype='str')
    for index in each_index(paper):
        if index in dots:
            paper[index] = 'X'
        else:
            paper[index] = ' '
    return paper


def solve(input: list[str]) -> tuple[int, NDArray]:
    dots = get_dots(input)
    folds = get_folds(input)
    # first fold
    dots = do_fold(folds.pop(), dots)
    visible_dots = len(dots)
    # finish folding
    while len(folds) >= 1:
        dots = do_fold(folds.pop(), dots)
    return visible_dots, make_paper(dots)
