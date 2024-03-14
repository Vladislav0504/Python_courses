"""Exam."""
from sys import stdin


def main():
    """My function."""
    num_m, _ = int(input()), input()
    maths = {stdin.readline().strip() for _ in range(num_m)}
    informatics = {line.strip() for line in stdin}
    print(len(maths.symmetric_difference(informatics)) or "NO")


if __name__ == "__main__":
    main()
