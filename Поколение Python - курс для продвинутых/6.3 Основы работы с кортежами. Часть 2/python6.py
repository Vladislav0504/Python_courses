"""Tuples."""
from sys import stdin


def main():
    """My function."""
    input()
    students = tuple(line.split() for line in stdin)
    print(*(f"{man} {mark}" for man, mark in students), sep="\n", end="\n\n")
    print(*(f"{man} {mark}" for man, mark in students if int(mark) > 3),
          sep="\n")


if __name__ == "__main__":
    main()
