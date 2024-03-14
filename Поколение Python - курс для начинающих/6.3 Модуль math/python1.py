"""Types."""


def main():
    """My function."""
    x_1, y_1, x_2, y_2 = (float(input()) for _ in range(4))
    print(((x_1 - x_2)**2 + (y_1 - y_2)**2)**0.5)


if __name__ == "__main__":
    main()
