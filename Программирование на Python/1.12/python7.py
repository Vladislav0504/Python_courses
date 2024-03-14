"""Problems."""


def main():
    """My function."""
    ticket = input()
    if sum(map(int, ticket[:3])) == sum(map(int, ticket[-3:])):
        print("Счастливый")
    else:
        print("Обычный")


if __name__ == "__main__":
    main()
