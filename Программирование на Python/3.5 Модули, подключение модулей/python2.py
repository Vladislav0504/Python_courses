"""Importing modules."""
from sys import argv


def main():
    """My function."""
    print(*argv[1:])


if __name__ == "__main__":
    main()
