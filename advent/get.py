
def input(year: int, day: int):
    with open(f"..\\..\\inputs\\{year}\\d{day}.txt", "r") as f:
        input = f.read().splitlines()
    return input


def sample(year: int, day: int):
    with open(f"..\\..\\samples\\{year}\\d{day}.txt", "r") as f:
        sample = f.read().splitlines()
    return sample
