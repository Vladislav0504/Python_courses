"""Loops."""


def main():
    """My function."""
    num, counter = int(input()), 0
    while 0 < num <= 5:
        counter += (num == 5)
        num = int(input())
    print(counter)


if __name__ == "__main__":
    main()
