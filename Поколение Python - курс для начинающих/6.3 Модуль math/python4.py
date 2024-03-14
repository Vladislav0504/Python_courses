"""Types."""
from math import sin, cos, tan, radians


def main():
    """My function."""
    num_x = float(input())
    rad_x = radians(num_x)
    print(sin(rad_x) + cos(rad_x) + (tan(rad_x))**2)


if __name__ == "__main__":
    main()
