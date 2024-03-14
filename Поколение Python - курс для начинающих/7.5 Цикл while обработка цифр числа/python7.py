"""Loops."""


def main():
    """My function."""
    num = list(map(int, input()))
    print("YES" if num == sorted(num, reverse=True) else "NO")


if __name__ == "__main__":
    main()
