"""Exam."""
from sys import stdin


def main():
    """My function."""
    reader = (line.strip() for line in stdin)
    num_m = int(next(reader))
    res = set.intersection(*({next(reader) for _ in range(int(next(reader)))}
                             for _ in range(num_m)))
    print(*sorted(res), sep="\n")


if __name__ == "__main__":
    main()
