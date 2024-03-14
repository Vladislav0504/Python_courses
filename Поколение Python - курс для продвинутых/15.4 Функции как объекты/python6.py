"""Functions."""


def main():
    """My function."""
    lst = input().split()
    print(*sorted(lst, key=lambda x: sum(map(int, x))))


if __name__ == "__main__":
    main()
