"""Functions."""


def print_initials(name: str, surname: str, patronymic: str) -> None:
    """Person initials."""
    print("".join((surname[0], name[0], patronymic[0])).upper())


def main():
    """My function."""
    name, surname, patronymic = (input() for _ in range(3))
    print_initials(name, surname, patronymic)


if __name__ == "__main__":
    main()
