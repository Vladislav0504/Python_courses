"""Int function."""


def main():
    """My function."""
    num = int(input())
    print(*(num + i for i in range(3)), sep="\n")


if __name__ == "__main__":
    main()
