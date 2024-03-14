"""Print function."""


def main():
    """My function."""
    sep = input()
    lst = [input() for _ in range(3)]
    print(*lst, sep=sep)


if __name__ == "__main__":
    main()
