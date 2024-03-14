"""Exam."""


def main():
    """My function."""
    x_1, y_1, x_2, y_2 = (int(input()) for _ in range(4))
    print("YES" if x_1 + y_1 & 1 == x_2 + y_2 & 1 else "NO")


if __name__ == "__main__":
    main()
