"""Exam."""
from sys import stdin

from functools import reduce


def main():
    """My function."""
    reader = (line.strip() for line in stdin)
    next(reader)
    print(*sorted(reader, key=lambda ip: reduce(lambda x, y: (x << 8) + y,
                                                map(int, ip.split(".")), 0)),
          sep="\n")


if __name__ == "__main__":
    main()
