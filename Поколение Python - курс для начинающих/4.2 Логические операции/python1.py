"""Conditions."""


def main():
    """My function."""
    num_x, limits = int(input()), (-1, 17)
    print("Принадлежит" if limits[0] < num_x < limits[1] else "Не принадлежит")


if __name__ == "__main__":
    main()
