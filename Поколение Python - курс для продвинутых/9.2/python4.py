"""Exam."""
from sys import stdin


def main():
    """My function."""
    num_m, _ = int(input()), input()
    library = {stdin.readline().strip() for _ in range(num_m)}
    print(*("YES" if line.strip() in library else "NO" for line in stdin),
          sep="\n")


if __name__ == "__main__":
    main()
