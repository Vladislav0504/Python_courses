"""Lists."""


def main():
    """My function."""
    numbers = input().split()
    lst = [int(i)**3 for i in numbers]
    print(*lst)


if __name__ == "__main__":
    main()
