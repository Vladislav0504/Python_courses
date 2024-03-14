"""Matrices."""


def main():
    """My function."""
    num_n, num_m = map(int, input().split())
    matrix = tuple(tuple(1 + j % num_m for j in range(i, num_m + i))
                   for i in range(num_n))
    for row in matrix:
        print(*(x + " " * (3 - len(x)) for x in map(str, row)), sep="")


if __name__ == "__main__":
    main()
