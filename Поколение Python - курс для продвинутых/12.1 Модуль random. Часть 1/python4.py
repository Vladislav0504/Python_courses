"""Random."""
from random import sample


def main():
    """My function."""
    maximum = 49
    numbers_for_ticket = sample(range(1, maximum + 1), 7)
    print(*sorted(numbers_for_ticket))


if __name__ == "__main__":
    main()
