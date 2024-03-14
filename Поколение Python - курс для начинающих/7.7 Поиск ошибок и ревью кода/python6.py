"""Loops."""


def main():
    """My function."""
    prod = 1
    for k in map(int, input()):
        prod *= k
    print(prod)


if __name__ == "__main__":
    main()
