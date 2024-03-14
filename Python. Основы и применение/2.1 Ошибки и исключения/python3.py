"""Errors and exceptions.

Good program.
"""
from typing import List


class NonPositiveError(Exception):
    """NonPositiveError exception."""

    def __init__(self, num_x: int) -> None:
        """Non-positive error constructor."""
        super().__init__()
        self.num = num_x

    def __str__(self) -> str:
        """Display information."""
        return f"A non-positive number {self.num} is added!"


class PositiveList(List):
    """Positive integer numbers."""

    def __init__(self, *iterable: int) -> None:
        """Positive list constructor."""
        super().__init__(*iterable)
        self.append_count = 0

    def append(self, num_x: int) -> None:
        """Append num_x."""
        if num_x <= 0:
            raise NonPositiveError(num_x)
        super().append(num_x)
        self.append_count += 1


def main():
    """My function."""
    try:
        lst = PositiveList()
        print(lst, lst.append_count)
        lst.append(5)
        print(lst, lst.append_count)
        lst.append(-2)
    except NonPositiveError as exc:
        print(exc)


if __name__ == "__main__":
    main()
