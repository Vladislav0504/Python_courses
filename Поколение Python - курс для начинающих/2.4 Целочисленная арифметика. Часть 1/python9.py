"""Int function."""


def main():
    """My function."""
    num_x = int(input())
    print(*(num_x * i for i in range(1, 6)), sep="---")


if __name__ == "__main__":
    main()
