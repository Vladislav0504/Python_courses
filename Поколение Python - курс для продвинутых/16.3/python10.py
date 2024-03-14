"""Exam."""
from sys import stdin


def main():
    """My function."""
    reader = (line.strip() for line in stdin)
    next(reader)
    print(*sorted(reader, key=lambda w: (sum(map(lambda c: ord(c) - ord("A"),
                                                 w.upper())), w)), sep="\n")


if __name__ == "__main__":
    main()
