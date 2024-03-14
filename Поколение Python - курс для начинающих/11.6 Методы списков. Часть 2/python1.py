"""Lists."""


def main():
    """My function."""
    numbers, num_5 = [8, 9, 10, 11], 25
    numbers[1] = 17
    numbers.extend([4, 5, 6])
    numbers.pop(0)
    numbers *= 2
    numbers.insert(3, num_5)
    print(numbers)


if __name__ == "__main__":
    main()
