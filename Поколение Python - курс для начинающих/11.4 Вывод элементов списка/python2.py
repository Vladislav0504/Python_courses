"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst = [int(input()) for _ in range(num_n)]
    print(*lst, sep="\n", end="\n\n")
    print(*((x + 1)**2 for x in lst), sep="\n")


if __name__ == "__main__":
    main()
