"""Conditions."""


def main():
    """My function."""
    num, limits = int(input()), (0, 11, 19, 29, 36)
    if num < limits[0] or num > limits[4]:
        print("ошибка ввода")
    elif num == limits[0]:
        print("зеленый")
    elif (num < limits[1] or limits[2] <= num < limits[3]) + (num & 1) == 1:
        print("черный")
    else:
        print("красный")


if __name__ == "__main__":
    main()
