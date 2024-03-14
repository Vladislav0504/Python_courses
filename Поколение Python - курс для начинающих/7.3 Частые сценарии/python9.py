"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    max_1, max_2 = int(input()), 0
    for _ in range(num_n - 1):
        num = int(input())
        if num > max_1:
            max_1, max_2 = num, max_1
        elif num > max_2:
            max_2 = num
    print(max_1, max_2, sep="\n")


if __name__ == "__main__":
    main()
