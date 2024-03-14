"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst = [list(range(1, i + 1)) for i in range(1, num_n + 1)]
    print(*lst, sep="\n")


if __name__ == "__main__":
    main()
