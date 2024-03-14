"""Array. Stack. Queue."""


def sum_numbers(filename: str) -> int:
    """Sum numbers."""
    with open(filename, "r", encoding="utf8") as file:
        return sum(int(line) for line in file)


def main():
    """My function."""
    print(sum_numbers("numbers.txt"))


if __name__ == "__main__":
    main()
