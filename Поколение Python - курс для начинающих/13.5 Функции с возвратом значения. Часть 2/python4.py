"""Functions."""


def is_password_good(password: str) -> bool:
    """Is password good?."""
    condition_1 = len(password) >= 8
    condition_2 = any(char.isalpha() and char.isupper() for char in password)
    condition_3 = any(char.isalpha() and char.islower() for char in password)
    condition_4 = any(char.isdigit() for char in password)
    return all((condition_1, condition_2, condition_3, condition_4))


def main():
    """My function."""
    txt = input()
    print(is_password_good(txt))


if __name__ == "__main__":
    main()
