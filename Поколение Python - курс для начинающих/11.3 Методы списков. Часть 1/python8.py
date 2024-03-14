"""Lists."""


def main():
    """My function."""
    num_n = int(input())
    lst = [input() for _ in range(num_n)]
    num_k = int(input())
    print(*[s[num_k - 1:num_k] for s in lst], sep="")


if __name__ == "__main__":
    main()
