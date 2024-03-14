"""Functions."""
from typing import TypeVar

T = TypeVar("T")


def mean(*args: T) -> float:
    """Mean of int and float arguments."""
    total, count = 0, 0
    for arg in args:
        my_type = type(arg)
        if my_type in (int, float):
            total += arg
            count += 1
    if count == 0:
        return 0
    return total / count


def main():
    """My function."""
    assert mean() == 0
    assert mean(7) == 7
    assert mean(1.5, True, ["stepik"], "beegeek", 2.5, (1, 2)) == 2
    assert mean(True, ["stepik"], "beegeek", (1, 2)) == 0
    assert mean(-1, 2, 3, 10, ("5",)) == 3.5
    assert mean(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) == 5.5


if __name__ == "__main__":
    main()
