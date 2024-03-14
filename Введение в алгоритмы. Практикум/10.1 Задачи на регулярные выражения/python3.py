"""Regular expressions."""
from re import findall

from sys import stdin


def main():
    """My function."""
    print(*findall(r"\w+@\w+\.\w+", stdin.read()))


if __name__ == "__main__":
    main()
