"""Lists."""


def main():
    """My function."""
    numbers = input().split()
    print(*("+" * k for k in map(int, numbers)), sep="\n")


if __name__ == "__main__":
    main()
