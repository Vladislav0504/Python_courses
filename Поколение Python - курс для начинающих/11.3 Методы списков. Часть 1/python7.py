"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst = [int(input()) for _ in range(num_n)]
    del lst[1::2]
    print(lst)


if __name__ == "__main__":
    main()
