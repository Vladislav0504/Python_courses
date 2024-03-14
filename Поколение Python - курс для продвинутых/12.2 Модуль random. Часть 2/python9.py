"""Random."""
from random import choice, shuffle

from string import ascii_lowercase, ascii_uppercase, digits


def generate_password(length: int) -> str:
    """Generate password."""
    ascii_up = list(set(ascii_uppercase) - set("IO"))
    ascii_low = list(set(ascii_lowercase) - set("lo"))
    dig = list(set(digits) - set("01"))
    alphabet = ascii_up + ascii_low + dig
    lst = [choice(elem) for elem in (ascii_up, ascii_low, dig)]
    lst.extend([choice(alphabet) for _ in range(length - 3)])
    shuffle(lst)
    return "".join(lst)


def generate_passwords(count: int, length: int) -> list[str]:
    """Generate passwords."""
    return [generate_password(length) for _ in range(count)]


def main():
    """My function."""
    num_n, num_m = int(input()), int(input())
    passwords = generate_passwords(num_n, num_m)
    print(*passwords, sep="\n")


if __name__ == "__main__":
    main()
