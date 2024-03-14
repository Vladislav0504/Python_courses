"""Lists."""


def main():
    """My function."""
    rainbow = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
    rainbow[rainbow.index("Green")] = "Зеленый"
    rainbow[rainbow.index("Violet")] = "Фиолетовый"
    print(rainbow)


if __name__ == "__main__":
    main()
