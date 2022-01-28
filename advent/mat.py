
"""Helper classes and functions to deal wth 2d arrays.
"""

import numpy as np
from numpy.typing import NDArray
from typing import NewType


CartesianIndex = NewType("CartesianIndex", tuple[int, int])


def as_matrix(input: list[str]) -> NDArray:
    """Return input as a two dimensional integer array.
    """
    arr = [line[x] for line in input for x in range(len(line))]
    return np.array(arr, dtype=int).reshape(len(input), len(input[0]))


def each_index(matrix: NDArray) -> CartesianIndex:
    """Generator function. Return the indices of the given matrix.
    This is a row major function.
    """
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            yield (i, j)


def in_bounds(matrix: NDArray, index: CartesianIndex) -> bool:
    """Return True if the index is within the boundaries of the matrix.
    Otherwise return False.
    """
    x, y = index
    m, n = matrix.shape
    return x >= 0 and x < m and y >= 0 and y < n


def each_neighbour(matrix: NDArray, index: CartesianIndex) -> list[CartesianIndex]:
    """Return the neighbours of the given neighbours.

    This is a row major function.
    """
    neighbours = []
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            else:
                neighbour = index[0] + dx, index[1] + dy
                if in_bounds(matrix, neighbour):
                    neighbours.append(neighbour)
    return neighbours


def each_nearest_neighbour(matrix: NDArray, index: CartesianIndex) -> list[CartesianIndex]:
    neighbours = []
    x, y = index
    if in_bounds(matrix, (x-1, y)):
        neighbours.append((x-1, y))
    if in_bounds(matrix, (x+1, y)):
        neighbours.append((x+1, y))
    if in_bounds(matrix, (x, y-1)):
        neighbours.append((x, y-1))
    if in_bounds(matrix, (x, y+1)):
        neighbours.append((x, y+1))
    return neighbours


def are_diag(index: CartesianIndex, neighbour: CartesianIndex) -> bool:
    """Return True if index and neighbour are diagonal to each other.
    Otherwise return False.
    """
    dx, dy = index[0] - neighbour[0], index[1] - neighbour[1]
    if dx != 0 and dy != 0:
        return True
    else:
        return False
