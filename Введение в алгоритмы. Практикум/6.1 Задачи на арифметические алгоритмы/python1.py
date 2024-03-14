"""Arithmetic algorithms."""
from typing import Callable


class Solution:
    """Solution."""

    __methods = {"countPrimes": "count_primes",
                 "isHorrible": "is_horrible",
                 "isPerfectSquare": "is_perfect_square"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @staticmethod
    def count_primes(num_n: int) -> int:
        """Count primes."""
        lst = [True] * num_n
        lst[:2] = [False, False]
        if num_n > 1:
            for num in range(2, int(num_n**0.5) + 1):
                if lst[num]:
                    start = num**2
                    lst[start::num] = [False] * len(lst[start::num])
        return sum(lst)

    @staticmethod
    def is_horrible(num_n: int) -> bool:
        """Is horrible?."""
        if -1 <= num_n <= 1:
            return False
        for i in (2, 3, 5):
            while num_n % i == 0:
                num_n //= i
        return -1 <= num_n <= 1

    @staticmethod
    def gcd(num_m: int, num_n: int) -> int:
        """Greatest common divisor."""
        while num_m:
            num_n, num_m = num_m, num_n % num_m
        return num_n

    @classmethod
    def lcm(cls, num_m: int, num_n: int) -> int:
        """Lowest common multiple."""
        return num_m * num_n // cls.gcd(num_m, num_n)

    @staticmethod
    def fastpw(num_n: int, num_m: int) -> int:
        """Binary raising to power."""
        result = 1
        while num_m:
            if num_m & 1:
                result *= num_n
            num_n *= num_n
            num_m >>= 1
        return result

    @staticmethod
    def is_perfect_square(num_n: int) -> bool:
        """Is perfect square?."""
        if num_n < 0:
            return False
        return pow(num_n, 0.5).is_integer()


def problem_1() -> None:
    """Problem 1."""
    assert Solution.count_primes(3) == 1
    assert Solution.count_primes(39) == 12


def problem_2() -> None:
    """Problem 2."""
    assert not Solution.is_horrible(0)
    assert not Solution.is_horrible(35)
    assert Solution.is_horrible(120)
    assert Solution.is_horrible(81)


def problem_3() -> None:
    """Problem 3."""
    assert Solution.gcd(9, 10) == 1
    assert Solution.gcd(9, 22) == 1


def problem_4() -> None:
    """Problem 4."""
    assert Solution.lcm(5, 10) == 10
    assert Solution.lcm(4, 28) == 28


def problem_5() -> None:
    """Problem 5."""
    assert Solution.fastpw(7, 8) == 5764801


def problem_6() -> None:
    """Problem 6."""
    assert Solution.is_perfect_square(0)
    assert not Solution.is_perfect_square(31)
    assert Solution.is_perfect_square(4)
    assert not Solution.is_perfect_square(454)


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
