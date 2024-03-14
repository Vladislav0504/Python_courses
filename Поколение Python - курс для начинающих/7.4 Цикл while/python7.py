"""Loops."""


def main():
    """My function."""
    cost, counter = int(input()), 0
    values = (25, 10, 5, 1)
    for value in values:
        if value <= cost:
            counter += cost // value
            cost %= value
    print(counter)


if __name__ == "__main__":
    main()
