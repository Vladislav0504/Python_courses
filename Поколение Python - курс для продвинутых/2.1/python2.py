"""Repetition."""


def main():
    """My function."""
    weight, height = float(input()), float(input())
    lower_threshold, upper_threshold = 18.5, 25
    body_mass_index = weight / height**2
    if body_mass_index > upper_threshold:
        print("Избыточная масса")
    elif body_mass_index < lower_threshold:
        print("Недостаточная масса")
    else:
        print("Оптимальная масса")


if __name__ == "__main__":
    main()
