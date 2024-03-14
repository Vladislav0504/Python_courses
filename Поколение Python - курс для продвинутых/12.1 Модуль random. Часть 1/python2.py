"""Random."""
from random import randint


def main():
    """My function."""
    num_n = int(input())
    print(*(randint(1, 6) for _ in range(num_n)), sep="\n")


if __name__ == "__main__":
    main()
