"""Problems."""


def main():
    """My function."""
    string = input()
    if string == "треугольник":
        a_side = float(input())
        b_side = float(input())
        c_side = float(input())
        per = (a_side + b_side + c_side) / 2
        print((per * (per - a_side) * (per - b_side) * (per - c_side))**0.5)
    elif string == "прямоугольник":
        a_side = int(input())
        b_side = int(input())
        print(a_side * b_side)
    else:
        delta = 0.14
        num_pi = 3 + delta
        radius = float(input())
        print(num_pi * radius**2)


if __name__ == "__main__":
    main()
