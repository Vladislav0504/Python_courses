"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst = [int(input()) for _ in range(num_n)]
    print(*filter(lambda x: x < 0, lst), sep="\n")
    print(*filter(lambda x: x == 0, lst), sep="\n")
    print(*filter(lambda x: x > 0, lst), sep="\n")


if __name__ == "__main__":
    main()
