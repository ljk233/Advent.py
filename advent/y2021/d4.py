
from ..solution import Solution
from ..mat import each_index
from heapq import heappush, nlargest, nsmallest
from math import inf
import numpy as np
from numpy.typing import NDArray


def numbers(line: str) -> tuple[dict, dict]:
    num2pos: dict = {}
    turn2num: dict = {}
    numbers = [int(digit) for digit in line.split(",")]
    for pos, number in enumerate(numbers):
        num2pos[number] = pos
        turn2num[pos] = number
    return num2pos, turn2num


def boards(input: list[str]) -> tuple[list, NDArray]:
    boards = []
    for i in range(0, len(input), 6):
        board = [input[j].split() for j in range(i, i+5)]
        boards.append(np.array(board, int))
    return np.array(boards, np.ndarray)


def get_turn_board(board: NDArray, num2pos: dict) -> NDArray:
    tb = np.zeros_like(board)
    for index in each_index(board):
        num = board[index]
        if num in num2pos.keys():
            tb[index] = num2pos[board[index]]
        else:
            tb[index] = inf
    return tb


def min_turns(turn_board) -> list[tuple]:
    min_turn = inf
    for index in range(5):
        row_turn = sorted([turn for turn in turn_board[index, :]])[-1]
        if row_turn < min_turn:
            min_turn = row_turn
        col_turn = sorted([turn for turn in turn_board[:, index]])[-1]
        if col_turn < min_turn:
            min_turn = col_turn
    return min_turn


def score(board: NDArray, turn: int, winning_num: int, num2turn: dict) -> int:
    sum_board = 0
    for index in each_index(board):
        if num2turn[board[index]] > turn:
            sum_board += board[index]
    return sum_board * winning_num


def solve(input: list[str]) -> Solution:
    num2turn, turn2num = numbers(input[0])
    B = boards(input[2:])

    nstates = []
    for index in range(B.shape[0]):
        board = B[index]
        tb = get_turn_board(board, num2turn)
        min_turn = min_turns(tb)
        heappush(nstates, (min_turn, turn2num[min_turn], index))

    first_turn, fist_winning_num, first_board = nsmallest(1, nstates)[0]
    last_turn, last_winning_num, last_board = nlargest(1, nstates)[0]

    return Solution(
        score(B[first_board], first_turn, fist_winning_num, num2turn),
        score(B[last_board], last_turn, last_winning_num, num2turn)
    )
