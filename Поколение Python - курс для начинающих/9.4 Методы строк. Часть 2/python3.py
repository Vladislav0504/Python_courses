"""Strings."""


def main():
    """My function."""
    num_n = int(input())
    count = sum(input().count("11") >= 3 for _ in range(num_n))
    print(count)


if __name__ == "__main__":
    main()
