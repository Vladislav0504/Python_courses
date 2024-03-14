"""Exam."""
from typing import Callable, TypeVar

T = TypeVar("T")
V = TypeVar("V")
U = TypeVar("U")


def compose(func_f: Callable[[T], V], func_g: Callable[[U], T]) -> V:
    """Compose."""
    return lambda x: func_f(func_g(x))


def add3(num_x: T) -> T:
    """Add 3."""
    return num_x + 3


def mul7(num_x: T) -> T:
    """Multiply by 7."""
    return num_x * 7


def main():
    """My function."""
    assert compose(mul7, add3)(1) == 28
    assert compose(add3, mul7)(2) == 17
    assert compose(mul7, str)(3) == "3333333"
    # assert compose(str, mul7)(5) == "35"


if __name__ == "__main__":
    main()
