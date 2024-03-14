"""Sets."""
from sys import stdin


def main():
    """My function."""
    _, unique = input(), set().union(*(word.strip().lower() for word in stdin))
    print(len(unique))


if __name__ == "__main__":
    main()
