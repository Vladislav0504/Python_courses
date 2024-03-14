"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst = [list(range(1, num_n + 1)) for _ in range(num_n)]
    print(*lst, sep="\n")


if __name__ == "__main__":
    main()
