"""Functions."""


def get_middle_point(x_1: int, y_1: int, x_2: int, y_2: int) -> (float, float):
    """Middle point."""
    return (x_1 + x_2) / 2, (y_1 + y_2) / 2


def main():
    """My function."""
    x_1, y_1, x_2, y_2 = (int(input()) for _ in range(4))
    coord_x, coord_y = get_middle_point(x_1, y_1, x_2, y_2)
    print(coord_x, coord_y)


if __name__ == "__main__":
    main()
