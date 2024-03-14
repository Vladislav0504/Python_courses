"""Strings."""


def main():
    """My function."""
    num_a, num_b = int(input()), int(input())
    print(*map(chr, range(num_a, num_b + 1)))


if __name__ == "__main__":
    main()
