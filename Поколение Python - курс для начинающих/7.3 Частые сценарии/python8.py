"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    print((-1)**(num_n & 1 == 0) * (num_n + 1 >> 1))


if __name__ == "__main__":
    main()
