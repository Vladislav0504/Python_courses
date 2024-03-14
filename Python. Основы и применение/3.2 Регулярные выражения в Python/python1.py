"""Regular expressions."""
from sys import stdin

from re import search


def main():
    """My function."""
    print(*(line for line in stdin if search("cat.*cat", line)), sep="")


if __name__ == "__main__":
    main()
