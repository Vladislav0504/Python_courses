"""Loops."""


def main():
    """My function."""
    total = 1
    for _ in range(10):
        num = int(input())
        total *= num + (num == 0)
    print(total)


if __name__ == "__main__":
    main()
