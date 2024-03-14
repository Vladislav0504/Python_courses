"""Strings."""


def main():
    """My function."""
    string, count_1, count_2 = input(), 0, 0
    for char in string.lower():
        if char in "ауоыиэяюе":
            count_1 += 1
        elif char in "бвгджзйклмнпрстфхцчшщ":
            count_2 += 1
    print(f"Количество гласных букв равно {count_1}")
    print(f"Количество согласных букв равно {count_2}")


if __name__ == "__main__":
    main()
