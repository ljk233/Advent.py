
# 2021, Day 4: Giant Squid
# %timeit = 230 ms ± 1.91 ms

# %%
from collections import namedtuple, deque
from typing import NamedTuple
import numpy as np
from numpy.typing import NDArray


sol = namedtuple('Solution', ['part1', 'part2'])


def make_seq_boards(input: list[str]) -> tuple[deque, NDArray]:
    seq = deque([int(digit) for digit in input[0].split(",")])
    boards = []
    for i in range(2, len(input), 6):
        board = [input[j].split() for j in range(i, i+5)]
        boards.append(np.array(board, int))
    return seq, np.array(boards, np.ndarray)


def is_finished(board: NDArray) -> bool:
    for i in range(5):
        if np.sum(board[i, :]) == -5 or np.sum(board[:, i]) == -5:
            return True
    return False


def play_bingo(boards: NDArray, numbers: deque[int]) -> list[tuple[NDArray, int]]:
    playing = [i for i in range(0, boards.shape[0])]
    finished = []
    while len(playing) >= 1:
        number = numbers.popleft()
        still_playing = []
        for idx in playing:
            boards[idx] = np.where(boards[idx] == number, -1, boards[idx])
            if is_finished(boards[idx]):
                finished.append((boards[idx], number))
            else:
                still_playing.append(idx)
        playing = still_playing
    return finished


def score(nstate: tuple[NDArray, int]) -> int:
    board, number = nstate
    board = np.where(board==-1, 0, board)
    return board.sum() * number


def solve(f: str) -> NamedTuple:
    with open(f, "r") as f:
        input: list[str] = f.read().splitlines()
    seq, boards = make_seq_boards(input)
    nstate = play_bingo(boards, seq)
    return sol(score(nstate[0]), score(nstate[-1]))


print("SAMPLE: ", solve("sample.txt"))
print("INPUT:  ", solve("input.txt"))
