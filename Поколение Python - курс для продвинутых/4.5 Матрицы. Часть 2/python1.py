"""Matrices."""


def main():
    """My function."""
    num_n, num_m = int(input()), int(input())
    multiply = (tuple([0] * num_m),
                *(tuple(range(0, num_m * i, i)) for i in range(1, num_n)))
    for row in multiply:
        print(*(k + " " * (3 - len(k)) for k in map(str, row)), sep="")


if __name__ == "__main__":
    main()
