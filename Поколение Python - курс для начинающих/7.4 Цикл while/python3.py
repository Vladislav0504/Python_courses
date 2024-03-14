"""Loops."""


def main():
    """My function."""
    counter = 0
    while input() not in ("стоп", "хватит", "достаточно"):
        counter += 1
    print(counter)


if __name__ == "__main__":
    main()
