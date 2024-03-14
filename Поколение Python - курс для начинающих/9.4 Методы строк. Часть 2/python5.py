"""Strings."""


def main():
    """My function."""
    string = input()
    print("YES" if string.endswith(".com") or string.endswith(".ru") else "NO")


if __name__ == "__main__":
    main()
