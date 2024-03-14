"""Functions."""


def main():
    """My function."""
    limit = 255
    print(*map(lambda x: limit - int(x), input().split()))


if __name__ == "__main__":
    main()
