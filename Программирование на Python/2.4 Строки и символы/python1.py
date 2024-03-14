"""Strings."""


def main():
    """My function."""
    genome = input()
    count = sum((char in "gGcC") for char in genome)
    print(count * 100 / len(genome))


if __name__ == "__main__":
    main()
