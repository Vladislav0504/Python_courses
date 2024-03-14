"""Loops."""
from sys import stdin


def main():
    """My function."""
    total = sum(num for num in map(int, stdin) if num & 1 == 0)
    print(total)


if __name__ == "__main__":
    main()
