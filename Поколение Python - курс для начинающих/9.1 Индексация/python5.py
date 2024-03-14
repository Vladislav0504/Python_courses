"""Strings."""


def main():
    """My function."""
    first_name, last_name, patronymic = (input() for _ in range(3))
    print(last_name[0], first_name[0], patronymic[0], sep="")


if __name__ == "__main__":
    main()
