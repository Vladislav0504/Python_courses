"""Conditions."""


def main():
    """My function."""
    num, div, limits = int(input()), (7, 17), (999, 10000)
    if 0 in (num % div[0], num % div[1]) and limits[0] < num < limits[1]:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
