"""Functions."""


def is_valid_triangle(l_1: int, l_2: int, l_3: int) -> bool:
    """Is triangle valid?."""
    return l_1 + l_2 > l_3 and l_2 + l_3 > l_1 and l_3 + l_1 > l_2


def main():
    """My function."""
    side_1, side_2, side_3 = (int(input()) for _ in range(3))
    print(is_valid_triangle(side_1, side_2, side_3))


if __name__ == "__main__":
    main()
