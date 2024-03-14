"""Bool type."""


def func(num_1: int, num_2: int) -> bool:
    """Divisibility."""
    return num_1 % num_2 == 0


def main():
    """My function."""
    num_1, num_2 = int(input()), int(input())
    print("делится" if func(num_1, num_2) else "не делится")


if __name__ == "__main__":
    main()
