"""Functions."""
from typing import Callable, TypeVar

T = TypeVar("T")
Y = TypeVar("Y")


def func_apply(function: Callable[[T], Y], lst: list[T]) -> list[Y]:
    """Apply function to all elements of list."""
    return list(map(function, lst))


def add3(num_x: float) -> float:
    """Add 3."""
    return num_x + 3


def mul7(num_x: float) -> float:
    """Multiply 7."""
    return num_x * 7


def main():
    """My function."""
    assert func_apply(mul7, [1, 2, 3, 4, 5, 6]) == [7, 14, 21, 28, 35, 42]
    assert func_apply(add3, [1, 2, 3, 4, 5, 6]) == [4, 5, 6, 7, 8, 9]
    assert func_apply(str, [1, 2, 3, 4, 5, 6]) == ["1", "2", "3", "4", "5",
                                                   "6"]


if __name__ == "__main__":
    main()
