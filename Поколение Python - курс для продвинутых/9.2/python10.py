"""Exam."""
from sys import stdin


def main():
    """My function."""
    input()
    input()
    students = [line.strip() for line in stdin]
    k = (len(set(students)) << 1) - len(students)
    print(k or "NO")


if __name__ == "__main__":
    main()
