"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst, num_k = [input() for _ in range(num_n)], int(input())
    searches = [input().lower() for _ in range(num_k)]
    print(*(s for s in lst if all(x in s.lower() for x in searches)), sep="\n")


if __name__ == "__main__":
    main()
