"""Loops."""


def main():
    """My function."""
    num_m, num_n, div = int(input()), int(input()), (10, 15, 17)
    print(*(i for i in range(num_m, num_n + 1)
            if 0 in (i % div[1], i % div[2]) or i % div[0] == 9), sep="\n")


if __name__ == "__main__":
    main()
