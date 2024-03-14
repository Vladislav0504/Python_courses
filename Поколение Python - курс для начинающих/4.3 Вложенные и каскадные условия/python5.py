"""Conditions."""


def main():
    """My function."""
    weight, weights = int(input()), (60, 64, 69)
    if weight < weights[0]:
        print("Легкий вес")
    elif weight < weights[1]:
        print("Первый полусредний вес")
    else:
        print("Полусредний вес")


if __name__ == "__main__":
    main()
