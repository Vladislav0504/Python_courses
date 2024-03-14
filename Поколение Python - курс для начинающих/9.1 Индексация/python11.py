"""Strings."""


def main():
    """My function."""
    num, result = int(input()), []
    while num:
        result.append(num & 1)
        num >>= 1
    print(*result[::-1], sep="")


if __name__ == "__main__":
    main()
