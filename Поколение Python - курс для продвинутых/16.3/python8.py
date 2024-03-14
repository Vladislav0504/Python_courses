"""Exam."""
from typing import Callable, TypeVar

T = TypeVar("T")


def arithmetic_operation(operation: str) -> Callable[[T, T], T]:
    """Arithmetic operation."""
    my_dict = {"+": "__add__", "-": "__sub__", "*": "__mul__",
               "/": "__truediv__"}
    return getattr(int, my_dict[operation])


def main():
    """My function."""
    add = arithmetic_operation("+")
    div = arithmetic_operation("/")
    assert add(10, 20) == 30
    assert div(20, 5) == 4


if __name__ == "__main__":
    main()
