"""Strings."""


def main():
    """My function."""
    string = input()
    print("Цифра" if any(map(lambda x: x.isdigit(), string)) else "Цифр нет")


if __name__ == "__main__":
    main()
