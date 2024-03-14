"""Combinatorics."""
from typing import Callable


class Solution:
    """Solution."""

    __methods = {"letterCombinations": "letter_combinations",
                 "combinationSum": "combination_sum"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @classmethod
    def permutations(cls, numbers: list[int]) -> list[list[int]]:
        """Permutations."""
        if len(numbers) <= 1:
            return [numbers]
        my_set, result = set(), []
        for i, num in enumerate(numbers):
            if num not in my_set:
                my_set.add(num)
                lst = cls.permutations(numbers[:i] + numbers[i + 1:])
                result.extend([lst_i + [num] for lst_i in lst])
        return result

    @staticmethod
    def combine(num_n: int, num_k: int) -> list[list[int]]:
        """Combine."""
        if num_k > num_n:
            return []
        current = list(range(1, num_k + 1))
        result = [current.copy()]
        start = num_k - 1
        while start >= 0:
            while num_n - current[start] - (num_k - 1 - start) <= 0:
                start -= 1
                if start == -1:
                    break
            else:
                current[start] += 1
                for i in range(start + 1, num_k):
                    current[i] = current[i - 1] + 1
                result.append(current.copy())
                start = num_k - 1
        return result

    @staticmethod
    def letter_combinations(number: str) -> list[str]:
        """Letter combinations."""
        keys = (None, None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv",
                "wxyz")
        variants = [""]
        for i in map(int, number):
            variants = [var + char for var in variants for char in keys[i]]
        return variants

    @classmethod
    def combination_sum(cls, nums: list[int], target: int, repeat: bool = True,
                        start: bool = True) -> list[list[int]]:
        """Combine."""
        if start and nums:
            nums.sort(reverse=True)
            if nums[-1] == 0:
                nums.pop()
        if target == 0:
            return [[]]
        result, my_set = [], set()
        for i, num in enumerate(nums):
            if target >= num and num not in my_set:
                my_set.add(num)
                lst = cls.combination_sum(nums[i + 1 - repeat:], target - num,
                                          repeat, False)
                result.extend([lst_i + [num] for lst_i in lst])
        return result


def problem_1() -> None:
    """Problem 1."""
    lst = [1, 1, 2]
    result = [(2, 1, 1), (1, 2, 1), (1, 1, 2)]
    permutations = []
    for elem in Solution.permutations(lst):
        permutations.append(tuple(elem))
    assert len(permutations) == len(result)
    assert set(permutations) == set(result)


def problem_2() -> None:
    """Problem 2."""
    result = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    combinations = []
    for elem in Solution.combine(4, 2):
        combinations.append(tuple(elem))
    assert len(combinations) == len(result)
    assert set(combinations) == set(result)


def problem_3() -> None:
    """Problem 3."""
    strings = ["23", "36", "323", "72", "77"]
    results = [["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
               ["dm", "dn", "do", "em", "en", "eo", "fm", "fn", "fo"],
               ["dad", "dae", "daf", "dbd", "dbe", "dbf", "dcd", "dce", "dcf",
                "ead", "eae", "eaf", "ebd", "ebe", "ebf", "ecd", "ece", "ecf",
                "fad", "fae", "faf", "fbd", "fbe", "fbf", "fcd", "fce", "fcf"],
               ["pa", "pb", "pc", "qa", "qb", "qc", "ra", "rb", "rc", "sa",
                "sb", "sc"],
               ["pp", "pq", "pr", "ps", "qp", "qq", "qr", "qs", "rp", "rq",
                "rr", "rs", "sp", "sq", "sr", "ss"]]
    for string, result in zip(strings, results):
        solution = Solution.letter_combinations(string)
        assert len(solution) == len(result)
        assert set(solution) == set(result)


def problem_4() -> None:
    """Problem 4."""
    tests = [([2, 3, 6, 7], 7), ([2, 3, 5], 8), ([2], 2)]
    results = [[(2, 2, 3), (7,)], [(2, 2, 2, 2), (2, 3, 3), (3, 5)], [(2,)]]
    for test, result in zip(tests, results):
        solution = []
        for elem in Solution.combination_sum(*test):
            solution.append(tuple(elem))
        assert len(solution) == len(result)
        assert set(solution) == set(result)


def problem_5() -> None:
    """Problem 5."""
    tests = [([10, 1, 2, 7, 6, 1, 5], 8), ([2, 5, 2, 1, 2], 5)]
    results = [[(2, 6), (1, 1, 6), (1, 2, 5), (1, 7)], [(1, 2, 2), (5,)]]
    for test, result in zip(tests, results):
        solution = []
        for elem in Solution.combination_sum(*test, repeat=False):
            solution.append(tuple(elem))
        assert len(solution) == len(result)
        assert set(solution) == set(result)


def main():
    """My function."""
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()


if __name__ == "__main__":
    main()
