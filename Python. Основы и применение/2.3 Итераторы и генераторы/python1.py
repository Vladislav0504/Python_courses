"""Iterators and generators.

Good program.
"""
from typing import TypeVar, Generic, Iterable, Callable, Iterator

from sys import modules

T = TypeVar("T")
CLASS_NAME = "MultiFilter"


class MultiFilter(Generic[T]):
    """MultiFilter."""

    def __init__(self, iterable: Iterable[T],
                 *functions: Callable[[T], bool],
                 judge: Callable[[int, int], bool] = None) -> None:
        """Multifilter constructor."""
        self.iterable = iterable
        self.functions = functions
        self.judge = judge or self.judge_any

    def __iter__(self) -> Iterator[T]:
        """Return iterator over resulting sequence."""
        for elem in self.iterable:
            pos = sum(func(elem) for func in self.functions)
            if self.judge(pos, len(self.functions) - pos):
                yield elem

    def __repr__(self) -> str:
        """Representation."""
        return ", ".join((f"iterable = {self.iterable}",
                          f"functions = {self.functions}",
                          f"judge = {self.judge}"))

    @staticmethod
    def judge_any(pos: int, _) -> bool:
        """Allow element if at least one function allows it."""
        return pos >= 1

    @staticmethod
    def judge_half(pos: int, neg: int) -> bool:
        """Allow element if at least half of functions allow it."""
        return pos >= neg

    @staticmethod
    def judge_all(_, neg: int) -> bool:
        """Allow element if all functions allow it."""
        return neg == 0


multifilter = getattr(modules[__name__], CLASS_NAME)


def mul2(num_x: int) -> bool:
    """Is num_x divisible by 2?."""
    return num_x % 2 == 0


def mul3(num_x: int) -> bool:
    """Is num_x divisible by 3?."""
    return num_x % 3 == 0


def mul5(num_x: int) -> bool:
    """Is num_x divisible by 5?."""
    return num_x % 5 == 0


def main():
    """My function."""
    lst = list(range(31))  # [0, 1, 2, ... , 30]

    print(list(MultiFilter(lst, mul2, mul3, mul5)))
    # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26,
    # 27, 28, 30]

    print(list(multifilter(lst, mul2, mul3, mul5,
                           judge=multifilter.judge_half)))
    # [0, 6, 10, 12, 15, 18, 20, 24, 30]

    print(list(multifilter(lst, mul2, mul3, mul5,
                           judge=multifilter.judge_all)))
    # [0, 30]


if __name__ == "__main__":
    main()
