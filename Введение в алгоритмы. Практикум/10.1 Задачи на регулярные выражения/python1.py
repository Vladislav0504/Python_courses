"""Regular expressions."""
from re import findall

from sys import stdin


def main():
    """My function."""
    print(*findall(r"\d+", stdin.read()), sep=",")


if __name__ == "__main__":
    main()
