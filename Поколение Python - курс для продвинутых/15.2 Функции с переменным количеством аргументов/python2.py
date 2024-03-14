"""Functions."""
from typing import TypeVar

T = TypeVar("T")


def sq_sum(*args: T) -> T:
    """Sum of squares."""
    return sum(map(lambda x: x**2, args))


def main():
    """My function."""
    assert sq_sum() == 0
    assert sq_sum(2) == 4
    assert sq_sum(1.5, 2.5) == 8.5
    assert sq_sum(1, 2, 3) == 14
    assert sq_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 385


if __name__ == "__main__":
    main()
