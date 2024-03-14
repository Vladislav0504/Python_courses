"""Loops."""


def main():
    """My function."""
    num = input()
    first = int(num[0])
    print("YES" if all(k == first for k in map(int, num)) else "NO")


if __name__ == "__main__":
    main()
