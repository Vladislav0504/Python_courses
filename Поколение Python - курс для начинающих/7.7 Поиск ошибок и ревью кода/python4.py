"""Loops."""


def main():
    """My function."""
    max_digit = max((k for k in map(int, input()) if k % 3 == 0), default="NO")
    print(max_digit)


if __name__ == "__main__":
    main()
