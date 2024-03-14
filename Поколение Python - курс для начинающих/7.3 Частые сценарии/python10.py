"""Loops."""


def main():
    """My function."""
    print("NO" if any(int(input()) & 1 for _ in range(10)) else "YES")


if __name__ == "__main__":
    main()
