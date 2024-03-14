"""Functions."""
from typing import TypeVar

T = TypeVar("T")


def count_args(*args: T) -> int:
    """Count args."""
    return len(args)


def main():
    """My function."""
    assert count_args() == 0
    assert count_args(10) == 1
    assert count_args("stepik", "beegeek") == 2
    assert count_args([], ("",), "a", 12, False) == 5


if __name__ == "__main__":
    main()
