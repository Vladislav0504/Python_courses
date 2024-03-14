"""Lists."""


def main():
    """My function."""
    print(*(char for char in input() if char.isdigit()), sep="")


if __name__ == "__main__":
    main()
