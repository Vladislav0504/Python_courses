"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst = [int(input()) for _ in range(num_n)]
    lst.remove(min(lst))
    lst.remove(max(lst))
    print(*lst, sep="\n")


if __name__ == "__main__":
    main()
