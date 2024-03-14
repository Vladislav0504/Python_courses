"""Regular expressions."""
from sys import stdin

from re import sub


def main():
    """My function."""
    print(*(sub("human", "computer", line) for line in stdin), sep="")


if __name__ == "__main__":
    main()
