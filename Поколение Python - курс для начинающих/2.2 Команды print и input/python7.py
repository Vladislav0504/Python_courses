"""Input function."""


def main():
    """My function."""
    lst = [input() for _ in range(3)]
    print(*lst, sep="\n")


if __name__ == "__main__":
    main()
