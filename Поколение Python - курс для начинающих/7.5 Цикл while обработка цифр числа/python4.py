"""Loops."""


def main():
    """My function."""
    num = input()
    total, count, prod = sum(map(int, num)), len(num), 1
    first, first_last = num[0], int(num[0]) + int(num[-1])
    for k in map(int, num):
        prod *= k
    print(total, count, prod, total / count, first, first_last, sep="\n")


if __name__ == "__main__":
    main()
