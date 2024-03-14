"""Conditions."""


def main():
    """My function."""
    num_x, limits = int(input()), (-30, -2, 7, 25)
    if limits[0] < num_x <= limits[1] or limits[2] < num_x <= limits[3]:
        print("Принадлежит")
    else:
        print("Не принадлежит")


if __name__ == "__main__":
    main()
