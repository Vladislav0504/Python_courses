"""Exam."""
from typing import Callable, TypeVar

T = TypeVar("T")
V = TypeVar("V")


def call(function: Callable[..., V], *args: T) -> V:
    """Call function."""
    return function(*args)


def mul7(num_x: T) -> T:
    """Multiply by 7."""
    return num_x * 7


def add2(num_x: T, num_y: T) -> T:
    """Add two numbers."""
    return num_x + num_y


def add3(num_x: T, num_y: T, num_z: T) -> T:
    """Add three numbers."""
    return num_x + num_y + num_z


def main():
    """My function."""
    assert call(mul7, 10) == 70
    assert call(add2, 2, 7) == 9
    assert call(add3, 10, 30, 40) == 80
    assert not call(bool, 0)


if __name__ == "__main__":
    main()
