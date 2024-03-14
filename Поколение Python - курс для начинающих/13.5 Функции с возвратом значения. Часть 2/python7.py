"""Functions."""


def is_prime(num: int) -> bool:
    """Is number prime?."""
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_valid_password(password: str) -> bool:
    """Is password valid?."""
    parts = password.split(":")
    cond_1 = len(parts) == 3
    cond_2 = all(part.isdigit() and int(part) != 0 for part in parts)
    cond_3 = parts[0] == parts[0][::-1]
    cond_4 = is_prime(int(parts[1]))
    cond_5 = int(parts[2]) & 1 == 0
    return all((cond_1, cond_2, cond_3, cond_4, cond_5))


def main():
    """My function."""
    password = input()
    print(is_valid_password(password))


if __name__ == "__main__":
    main()
