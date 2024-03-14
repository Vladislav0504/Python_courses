"""Dynamic programming."""
from typing import Callable


class Solution:
    """Solution."""

    __methods = {"maxProfit": "max_profit",
                 "climbStairs": "climb_stairs",
                 "minCost": "min_cost",
                 "countBits": "count_bits"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @staticmethod
    def max_profit(costs: list[int], pay: int = 0, flag: bool = False) -> int:
        """Max profit."""
        without_share = 0
        if costs:
            with_share = -costs[0]
            for cost in costs:
                with_share = max(with_share, without_share * flag - cost)
                without_share = max(without_share, cost + with_share - pay)
        return without_share

    @staticmethod
    def climb_stairs(num_n: int) -> int:
        """Climb stairs."""
        count_0, count_1 = 1, 1
        for _ in range(num_n - 1):
            count_0, count_1 = count_1, count_0 + count_1
        return count_1

    @staticmethod
    def min_cost(costs: list[int]) -> int:
        """Min cost."""
        cost_0, cost_1 = 0, 0
        for price_0, price_1 in zip(costs, costs[1:]):
            cost_0, cost_1 = cost_1, min(cost_0 + price_0, cost_1 + price_1)
        return cost_1

    @staticmethod
    def rob(costs: list[int]) -> int:
        """Rob."""
        cost_0, cost_1 = 0, 0
        for cost in costs:
            cost_0, cost_1 = cost_1, max(cost_1, cost_0 + cost)
        return cost_1

    @staticmethod
    def count_bits(num_n: int) -> list[int]:
        """Count bits."""
        result = [0] * (num_n + 1)
        for number in range(1, num_n + 1):
            result[number] = result[number >> 1] + (number & 1)
        return result


def problem_1() -> None:
    """Problem 1."""
    assert Solution.max_profit([1, 4, 5, 0, 9, 3, 2]) == 9


def problem_2() -> None:
    """Problem 2."""
    assert Solution.climb_stairs(8) == 34


def problem_3() -> None:
    """Problem 3."""
    assert Solution.min_cost([10, 15, 20]) == 15


def problem_4() -> None:
    """Problem 4."""
    assert Solution.rob([9, 6, 5, 3, 2, 0, 4, 7, 8, 1]) == 28


def problem_5() -> None:
    """Problem 5."""
    assert Solution.count_bits(1) == [0, 1]


def problem_6() -> None:
    """Problem 6."""
    assert Solution.max_profit([1, 3, 2, 8, 4, 9], 2, flag=True) == 8


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
