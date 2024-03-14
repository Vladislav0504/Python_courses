"""Tuples."""


def main():
    """My function."""
    num_a, num_b, num_c = (int(input()) for _ in range(3))
    print((-num_b / (num_a << 1), num_c - num_b**2 / (num_a << 2)))


if __name__ == "__main__":
    main()
