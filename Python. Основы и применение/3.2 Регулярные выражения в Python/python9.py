"""Regular expressions."""
from sys import stdin

from re import sub


def main():
    """My function."""
    print(*(sub(r"(\w)\1+", r"\1", line) for line in stdin), sep="")


if __name__ == "__main__":
    main()
