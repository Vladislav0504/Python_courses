"""Loops."""


def main():
    """My function."""
    num_a, num_b = int(input()), int(input())
    num_a += (3 - num_a % 3) % 3
    num_b -= (num_b % 3) % 3
    print((num_a + num_b) / 2)


if __name__ == "__main__":
    main()
