"""Exam."""


def main():
    """My function."""
    num, limits = int(input()), (6, 20)
    print("YES" if num & 1 or limits[0] <= num <= limits[1] else "NO")


if __name__ == "__main__":
    main()
