"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    for i in range(1, num_n + 1):
        print(*(min(j, (i << 1) - j) for j in range(1, i << 1)), sep="")


if __name__ == "__main__":
    main()
