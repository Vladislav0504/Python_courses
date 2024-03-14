"""Sort."""
from typing import Callable


class Solution:
    """Solution."""

    __methods = {"mergeSort": "merge_sort",
                 "quickSort": "quick_sort"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @staticmethod
    def merge(arr_1: list[int], arr_2: list[int]) -> list[int]:
        """Merge."""
        array = []
        ind_1, ind_2 = 0, 0
        len_1, len_2 = len(arr_1), len(arr_2)
        while ind_1 < len_1 and ind_2 < len_2:
            if arr_1[ind_1] <= arr_2[ind_2]:
                array.append(arr_1[ind_1])
                ind_1 += 1
            else:
                array.append(arr_2[ind_2])
                ind_2 += 1
        array.extend(arr_1[ind_1:])
        array.extend(arr_2[ind_2:])
        return array

    @classmethod
    def merge_sort(cls, array: list[int]) -> list[int]:
        """Mergesort."""
        if len(array) > 1:
            mid = len(array) >> 1
            sort_1 = cls.merge_sort(array[:mid])
            sort_2 = cls.merge_sort(array[mid:])
            return cls.merge(sort_1, sort_2)
        return array

    @staticmethod
    def partition(array: list[int], num_p: int) -> int:
        """Partition."""
        i, flag = 0, False
        for k, elem in enumerate(array):
            if elem < num_p:
                if flag:
                    i += 1
                    array[i - 1], array[k], array[i] = elem, array[i], num_p
                else:
                    array[i], array[k] = elem, array[i]
                    i += 1
            elif elem == num_p:
                flag = True
                array[i], array[k] = elem, array[i]
        return i + 1

    @classmethod
    def quick_sort(cls, array: list[int]) -> list[int]:
        """Quick sort."""
        if len(array) < 2:
            return array
        i = cls.partition(array, array[0]) - 1
        result = cls.quick_sort(array[:i]) + [array[i]]
        return result + cls.quick_sort(array[i + 1:])


def problem_1() -> None:
    """Problem 1."""
    lst_1 = [4, 5, 6, 7, 8]
    lst_2 = [0, 1, 2, 3, 9]
    result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert Solution.merge(lst_1, lst_2) == result


def problem_2() -> None:
    """Problem 2."""
    lst = [6, 2, 5, 4, 8, 3, 7, 9, 1, 0]
    result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert Solution.merge_sort(lst) == result


def problem_3() -> None:
    """Problem 3."""
    lst_1, num_1 = [5, 1, 7, 9, 6], 6
    lst_2, num_2 = [13, 24, 8, 39, 35, 29, 14, 0, 5, 3], 24
    assert Solution.partition(lst_1, num_1) == 3
    assert Solution.partition(lst_2, num_2) == 7


def problem_4() -> None:
    """Problem 4."""
    lst = [4, 2, 1, 9, 0, 6, 5, 8, 3, 7]
    result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert Solution.quick_sort(lst) == result


def main():
    """My function."""
    problem_1()
    problem_2()
    problem_3()
    problem_4()


if __name__ == "__main__":
    main()
