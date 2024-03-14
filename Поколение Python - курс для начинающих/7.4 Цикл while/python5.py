"""Loops."""


def main():
    """My function."""
    num, total = int(input()), 0
    while num >= 0:
        total += num
        num = int(input())
    print(total)


if __name__ == "__main__":
    main()
