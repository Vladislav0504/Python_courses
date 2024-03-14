"""Lists."""


def main():
    """My function."""
    numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
    print(sum(num**2 for num in numbers))


if __name__ == "__main__":
    main()
