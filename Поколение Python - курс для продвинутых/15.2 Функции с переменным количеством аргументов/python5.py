"""Functions."""
from sys import stdout

from typing import TypeVar

T = TypeVar("T")


def print_products(*args: T) -> None:
    """Print products."""
    i = 0
    for arg in args:
        my_type = type(arg)
        if my_type is str and arg:
            i += 1
            stdout.write(f"{i}) {arg}\n")
    if i == 0:
        stdout.write("Нет продуктов")


def main():
    """My function."""
    print_products("Бананы", [1, 2], ("Stepik",), "Яблоки", "", "Макароны", 5,
                   True)
    # 1) Бананы
    # 2) Яблоки
    # 3) Макароны
    print_products([4], {}, 1, 2, {"Beegeek"}, "")
    # Нет продуктов


if __name__ == "__main__":
    main()
