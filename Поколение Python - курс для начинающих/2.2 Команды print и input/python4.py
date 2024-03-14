"""Print function."""


def main():
    """My function."""
    print(*("*" * i for i in range(1, 8)), sep="\n")


if __name__ == "__main__":
    main()
