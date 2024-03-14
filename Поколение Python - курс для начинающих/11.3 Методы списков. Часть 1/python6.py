"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst = [int(input()) for _ in range(num_n)]
    print(list(map(sum, zip(lst, lst[1:]))))


if __name__ == "__main__":
    main()
