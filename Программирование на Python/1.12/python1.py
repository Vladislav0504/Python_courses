"""Problems."""


def main():
    """My function."""
    a_side = int(input())
    b_side = int(input())
    c_side = int(input())
    per = (a_side + b_side + c_side) / 2
    square = (per * (per - a_side) * (per - b_side) * (per - c_side))**0.5
    print(square)


if __name__ == "__main__":
    main()
