"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    total = 1
    for i in range(1, num_n + 1):
        total *= i
    print(total)


if __name__ == "__main__":
    main()
