"""Search."""
from typing import Callable

from random import randint

from math import log

from fractions import Fraction

VERSION = 4
FIRST_BAD_VERSION = randint(1, VERSION)


def is_bad_version(version: int) -> bool:
    """Is bad version?."""
    return FIRST_BAD_VERSION <= version


class Solution:
    """Solution."""

    __methods = {"peakIndexInMountainArray": "peak_index_in_mountain_array",
                 "firstBadVersion": "first_bad_version",
                 "estimateBudget": "estimate_budget",
                 "nextGreatestLetter": "next_greatest_letter"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @staticmethod
    def search(nums: list[int], value: int) -> int:
        """Binary search."""
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + right >> 1
            if nums[mid] == value:
                return mid
            if nums[mid] > value:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    @staticmethod
    def peak_index_in_mountain_array(nums: list[int]) -> int:
        """Peak index in mountain array."""
        left, right, mid = 0, len(nums) - 1, 0
        while left <= right:
            mid = left + right >> 1
            if left == right:
                break
            if nums[mid] >= nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return mid

    @staticmethod
    def first_bad_version(num_n: int) -> int:
        """First bad version."""
        left, right, mid = 1, num_n, 1
        while left <= right:
            mid = left + right >> 1
            if left == right:
                break
            if is_bad_version(mid):
                right = mid
            else:
                left = mid + 1
        return mid

    @staticmethod
    def estimate_budget(num_n: int, num_k: int) -> int:
        """Estimate budget."""
        return int(log(num_n, 2) + 1) * num_k

    @staticmethod
    def next_greatest_letter(letters: list[str], char: str) -> str:
        """Next greatest letter."""
        length = len(letters)
        left, right, mid = 0, length, 0
        while left <= right:
            mid = left + right >> 1
            if left == right:
                break
            if letters[mid] <= char:
                left = mid + 1
            else:
                right = mid
        return letters[mid % length]

    @staticmethod
    def divide(dividend: int, divisor: int) -> int:
        """Divide."""
        return int(Fraction(dividend, divisor))


def problem_1() -> None:
    """Problem 1."""
    assert Solution.search([2, 3], 2) == 0


def problem_2() -> None:
    """Problem 2."""
    assert Solution.peak_index_in_mountain_array([1, 2, 3, 2]) == 2


def problem_3() -> None:
    """Problem 3."""
    assert Solution.first_bad_version(VERSION) == FIRST_BAD_VERSION


def problem_4() -> None:
    """Problem 4."""
    assert Solution.estimate_budget(9, 86) == 344


def problem_5() -> None:
    """Problem 5."""
    lst = ["d", "e", "f", "f", "h", "k", "l", "o", "w", "x"]
    assert Solution.next_greatest_letter(lst, "o") == "w"
    assert Solution.next_greatest_letter(lst, "x") == "d"


def problem_6() -> None:
    """Problem 6."""
    assert Solution.divide(100, 64) == 1


def main():
    """My function."""
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()
    problem_6()


if __name__ == "__main__":
    main()
