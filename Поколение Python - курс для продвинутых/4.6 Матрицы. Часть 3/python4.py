"""Matrices."""


def main():
    """My function."""
    num_n, num_m = map(int, input().split())
    matrix = tuple(tuple(range(i, num_m * num_n + i, num_n))
                   for i in range(1, num_n + 1))
    for row in matrix:
        print(*(x + " " * (3 - len(x)) for x in map(str, row)), sep="")


if __name__ == "__main__":
    main()
