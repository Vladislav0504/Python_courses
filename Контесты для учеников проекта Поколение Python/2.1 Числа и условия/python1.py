"""Contest."""


def main():
    """My function."""
    num = input()
    print("YES" if any(i == j for i, j in zip(num, num[1:])) else "NO")


if __name__ == "__main__":
    main()
