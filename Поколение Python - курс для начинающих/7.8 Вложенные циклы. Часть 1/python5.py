"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    print(*(f"{i}" * i for i in range(1, num_n + 1)), sep="\n")


if __name__ == "__main__":
    main()
