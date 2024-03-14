"""Repetition."""
from sys import stdin

from re import compile as re_compile


def main():
    """My function."""
    find, _ = re_compile("a.*n.*t.*o.*n"), input()
    print(*(i for i, line in enumerate(stdin, 1) if find.search(line)))


if __name__ == "__main__":
    main()
