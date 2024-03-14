"""Loops."""


def main():
    """My function."""
    num_a, num_b = int(input()), int(input())
    prod = num_a * num_b
    while num_a:
        num_b, num_a = num_a, num_b % num_a
    print(prod // num_b)


if __name__ == "__main__":
    main()
