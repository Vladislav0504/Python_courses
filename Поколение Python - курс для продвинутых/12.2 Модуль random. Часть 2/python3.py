"""Random."""
from random import shuffle


def main() -> list[list[int]]:
    """My function."""
    init = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    row, col, lst = len(init), len(init[0]), sum(init, [])
    shuffle(lst)
    return [lst[i:i + col] for i in range(0, row * col, col)]


if __name__ == "__main__":
    matrix = main()
    print(matrix)
