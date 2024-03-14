"""Input function."""


def main():
    """My function."""
    lst = [input() for _ in range(3)]
    print(*lst[::-1], sep="\n")


if __name__ == "__main__":
    main()
