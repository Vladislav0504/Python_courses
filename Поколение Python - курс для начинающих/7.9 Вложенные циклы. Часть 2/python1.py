"""Loops."""


def main():
    """My function."""
    num_n, count = int(input()), 1
    for i in range(1, num_n + 1):
        print(*range(count, count + i))
        count += i


if __name__ == "__main__":
    main()
