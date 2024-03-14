"""Conditions."""


def main():
    """My function."""
    num, limit = int(input()), 18
    print("Доступ запрещен" if num < limit else "Доступ разрешен")


if __name__ == "__main__":
    main()
