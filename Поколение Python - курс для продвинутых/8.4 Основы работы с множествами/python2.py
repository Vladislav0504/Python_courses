"""Sets."""


def main():
    """My function."""
    lst = [20, 6, 8, 18, 18, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 12, 8, 8, 10,
           4, 2, 2, 2, 16, 20]
    numbers = set(lst)
    average = sum(numbers) / len(numbers)
    print(average)


if __name__ == "__main__":
    main()
