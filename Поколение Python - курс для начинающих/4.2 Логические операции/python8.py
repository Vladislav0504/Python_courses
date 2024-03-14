"""Conditions."""


def main():
    """My function."""
    col_1, str_1, col_2, str_2 = (int(input()) for _ in range(4))
    if -1 <= col_1 - col_2 <= 1 and -1 <= str_1 - str_2 <= 1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
