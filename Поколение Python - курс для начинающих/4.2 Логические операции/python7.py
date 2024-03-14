"""Conditions."""


def main():
    """My function."""
    col_1, str_1, col_2, str_2 = (int(input()) for _ in range(4))
    if col_1 == col_2 and str_1 != str_2 or col_1 != col_2 and str_1 == str_2:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
