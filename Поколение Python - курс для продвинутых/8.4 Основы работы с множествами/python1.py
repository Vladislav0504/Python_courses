"""Sets."""


def main():
    """My function."""
    lst = [1.414, 12.5, 3.1416, 2.719, 9.8, 1.414, 1.1618, 1.324, 2.719, 1.324]
    numbers = set(lst)
    print(min(numbers) + max(numbers))


if __name__ == "__main__":
    main()
