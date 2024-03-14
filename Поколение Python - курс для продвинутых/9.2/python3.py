"""Exam."""
from sys import stdin


def main():
    """My function."""
    num_n = int(stdin.readline())
    cities = {stdin.readline().strip() for _ in range(num_n)}
    print("REPEAT" if stdin.readline().strip() in cities else "OK")


if __name__ == "__main__":
    main()
