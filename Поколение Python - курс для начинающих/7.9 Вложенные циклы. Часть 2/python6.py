"""Loops."""


def main():
    """My function."""
    num_n, total, factorial = int(input()), 0, 1
    for i in range(1, num_n + 1):
        factorial *= i
        total += factorial
    print(total)


if __name__ == "__main__":
    main()
