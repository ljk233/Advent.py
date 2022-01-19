
# 2021, Day 3: Binary Diagnostic
# %timeit = 1.52 ms ± 11.3 µs per loop

# %%
from collections import namedtuple


sol = namedtuple('Solution', ['part1', 'part2'])


# return the most common bit in the given rows of grid in the given col
def mode(grid: list[str], rows: list[int], col: int) -> int:
    m = 0
    for row in rows:
        if grid[row][col] == "1":
            m += 1
        else:
            m -= 1
    if m >= 0:
        return 1
    else:
        return 0


# return the power consumption of the submarine
def power_consumption(grid: list[str]) -> int:
    # recursive funtion to calculate the power concumption
    def search(rows: list[int], gamma: str, epsilon: str, col: int) -> str:
        if col == len(grid[1]):
            return int(gamma, base=2) * int(epsilon, base=2)
        else:
            if mode(grid, rows, col):
                return search(rows, gamma + "1", epsilon + "0", col+1)
            else:
                return search(rows, gamma + "0", epsilon + "1", col+1)

    return search([i for i in range(0, len(grid))], "", "", 0)


# return the power consumption of the submarine
def lsr(grid: list[str]) -> int:
    # recursive function to calculate the lsr.
    def search(rows: list[int], col: int, common: bool):
        if len(rows) == 1:
            return int(grid[rows[0]], base=2)
        else:
            if common:
                target = str(mode(grid, rows, col))
            else:
                target = str(int(not mode(grid, rows, col)))
            next_rows = [i for i in rows if grid[i][col] == target]
            return search(next_rows, col+1, common)

    o2_rating = search([i for i in range(0, len(grid))], 0, True)
    co2_rating = search([i for i in range(0, len(grid))], 0, False)
    return o2_rating * co2_rating


def solve(f: str) -> namedtuple:
    with open(f, "r") as f:
        input: list[str] = f.read().splitlines()
    return sol(power_consumption(input), lsr(input))


print("SAMPLE: ", solve("sample.txt"))
print("INPUT:  ", solve("input.txt"))
