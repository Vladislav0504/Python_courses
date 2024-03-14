"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst, search = [input() for _ in range(num_n)], input().lower()
    print(*(s for s in lst if search in s.lower()), sep="\n")


if __name__ == "__main__":
    main()
