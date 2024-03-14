"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst = [char for _ in range(num_n) for char in input()]
    print(lst)


if __name__ == "__main__":
    main()
