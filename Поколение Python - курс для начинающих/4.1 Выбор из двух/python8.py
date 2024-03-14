"""Conditions."""


def main():
    """My function."""
    age, limits = int(input()), [14, 25, 60]
    if age < limits[0]:
        print("детство")
    elif age < limits[1]:
        print("молодость")
    elif age < limits[2]:
        print("зрелость")
    else:
        print("старость")


if __name__ == "__main__":
    main()
