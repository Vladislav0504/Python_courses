"""Global optimization."""
from typing import Callable

from numpy import sin, cos, linspace


class Solution:
    """Solution."""

    def __getattr__(self, _: str) -> Callable:
        """Attribute correction."""
        return getattr(self, "minimum")

    @staticmethod
    def minimum(func: Callable[[float], float]) -> float:
        """Minimum."""
        iterations = 1000
        return min(map(func, linspace(0, 1, iterations)))


def func_1(time: float) -> float:
    """First function."""
    return 27 * sin(21 * time) + 41 * cos(16 * time)


def problem_1() -> None:
    """Problem 1."""
    result, epsilon = -65.8, 0.1
    assert abs(Solution.minimum(func_1) - result) <= epsilon


def main():
    """My function."""
    problem_1()


if __name__ == "__main__":
    main()
