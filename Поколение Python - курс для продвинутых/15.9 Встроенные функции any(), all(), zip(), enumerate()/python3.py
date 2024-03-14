"""Functions."""


def main():
    """My function."""
    x_axis, y_axis, z_axis = (map(float, input().split()) for _ in range(3))
    radius = 2
    print(all(x**2 + y**2 + z**2 <= radius**2
              for x, y, z in zip(x_axis, y_axis, z_axis)))


if __name__ == "__main__":
    main()
