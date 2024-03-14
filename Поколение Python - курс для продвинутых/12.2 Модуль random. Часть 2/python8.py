"""Random."""
from random import choice

from string import ascii_letters, digits


def generate_password(length: int, chars: list[str]) -> str:
    """Generate password."""
    return "".join(choice(chars) for _ in range(length))


def generate_passwords(count: int, length: int, chars: list[str]) -> list[str]:
    """Generate passwords."""
    return [generate_password(length, chars) for _ in range(count)]


def main():
    """My function."""
    num_n, num_m = int(input()), int(input())
    chars = list((set(ascii_letters) | set(digits)) - set("lI1oO0"))
    passwords = generate_passwords(num_n, num_m, chars)
    print(*passwords, sep="\n")


if __name__ == "__main__":
    main()
