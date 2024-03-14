"""Exam."""


def main():
    """My function."""
    x_1, y_1, x_2, y_2 = (int(input()) for _ in range(4))
    diff_x, diff_y = abs(x_1 - x_2), abs(y_1 - y_2)
    print("YES" if diff_x == diff_y or diff_x * diff_y == 0 else "NO")


if __name__ == "__main__":
    main()
