
from ..solution import Solution
from ..mat import as_matrix, each_index, each_neighbour
from numpy.typing import NDArray


def is_ready(energy: int) -> bool:
    return energy > 9


def tick(cavern: NDArray) -> int:
    cavern += 1
    flashed = set()
    ready = set([index for index in each_index(cavern) if is_ready(cavern[index])])

    while len(ready) >= 1:
        flashing = ready.pop()
        flashed.add(flashing)
        for neighbour in each_neighbour(cavern, flashing):
            cavern[neighbour] += 1
            if neighbour not in flashed and is_ready(cavern[neighbour]):
                ready.add(neighbour)

    for index in flashed:
        cavern[index] = 0

    return len(flashed)


def solve(input: list[str]) -> Solution:
    cavern = as_matrix(input)
    n_flashed = []
    ticks = 0
    still_synching = True
    while still_synching:
        ticks += 1
        n_flashed.append(tick(cavern))
        still_synching = n_flashed[-1] != cavern.size

    return Solution(sum(n_flashed[:100]), ticks)
