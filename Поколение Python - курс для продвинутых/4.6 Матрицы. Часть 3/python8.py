"""Matrices."""


def main():
    """My function."""
    num_n, num_m = map(int, input().split())
    matrix = tuple(list(range(i, num_m + i))
                   for i in range(1, num_n * num_m + 1, num_m))
    for line in matrix[1::2]:
        line.reverse()
    for row in matrix:
        print(*(x + " " * (3 - len(x)) for x in map(str, row)), sep="")


if __name__ == "__main__":
    main()
