"""Repetition."""


def main():
    """My function."""
    string = f"{input()} запретил букву "
    orders = sorted(map(ord, set(string)))
    print(string + chr(orders[1]))
    for i in range(2, len(orders)):
        string = string.replace(chr(orders[i - 1]), "")
        print(*string.split(), chr(orders[i]))


if __name__ == "__main__":
    main()
