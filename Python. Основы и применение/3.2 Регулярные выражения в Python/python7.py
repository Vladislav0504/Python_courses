"""Regular expressions."""
from sys import stdin

from re import sub


def main():
    """My function."""
    print(*(sub(r"\b[Aa]+\b", "argh", line, 1) for line in stdin), sep="")


if __name__ == "__main__":
    main()
