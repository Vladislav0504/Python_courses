"""Project."""


def main():
    """My function."""
    num = int(input())
    print(*(f(num).upper()[2:] for f in (bin, oct, hex)), sep="\n")


if __name__ == "__main__":
    main()
