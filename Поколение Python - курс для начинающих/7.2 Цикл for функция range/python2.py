"""Loops."""


def main():
    """My function."""
    num_m, num_n = int(input()), int(input())
    step = (num_m <= num_n) - (num_m > num_n)
    print(*range(num_m, num_n + step, step), sep="\n")


if __name__ == "__main__":
    main()
