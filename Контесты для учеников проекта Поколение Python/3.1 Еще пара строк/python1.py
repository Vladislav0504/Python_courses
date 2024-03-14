"""Contest."""
from re import fullmatch

from sys import stdin


def main():
    """My function."""
    pattern = r"(\(\d{3}\) |\d{3}-)\d{3}-\d{4}\s*"
    input()
    numbers = "".join(number for number in stdin if fullmatch(pattern, number))
    print(numbers or "All phone numbers are incorrect")


if __name__ == "__main__":
    main()
