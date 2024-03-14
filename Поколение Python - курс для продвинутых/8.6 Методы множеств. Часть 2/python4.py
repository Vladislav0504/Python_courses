"""Sets."""
from sys import stdin


def main():
    """My function."""
    reader = (set(map(int, line.strip())) for line in stdin)
    _, nums = next(reader), set.intersection(*reader)
    print(*sorted(nums))


if __name__ == "__main__":
    main()
