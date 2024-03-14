"""Sort."""
from typing import Callable


class ListNode:
    """ListNode."""

    def __init__(self, val: int) -> None:
        """Node constructor."""
        self.val = val
        self.next = None

    def value(self) -> int:
        """Value."""
        return self.val

    def next_node(self) -> "ListNode":
        """Next node."""
        return self.next


class Solution:
    """Solution."""

    __methods = {"bubbleSwapCount": "bubble_swap_count",
                 "sortArray": "sort_array",
                 "isAnagram": "is_anagram",
                 "allCellsDistOrder": "all_cells_dist_order",
                 "sortList": "sort_list",
                 "largestPerimeter": "largest_perimeter"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @staticmethod
    def bubble_swap_count(array_a: list[int]) -> int:
        """Bubble swap count."""
        k, length = 0, len(array_a)
        for i in range(length):
            for j in range(length - i - 1):
                if array_a[j] > array_a[j + 1]:
                    array_a[j], array_a[j + 1] = array_a[j + 1], array_a[j]
                    k += 1
        return k

    @staticmethod
    def sort_array(array_a: list[int]) -> list[int]:
        """Sort array."""
        func = sorted
        array_1 = func(list(filter(lambda x: x & 1 == 0, array_a)))
        array_2 = func(list(filter(lambda x: x & 1, array_a)), reverse=True)
        array_a[::2], array_a[1::2] = array_1, array_2
        return array_a

    @staticmethod
    def is_anagram(string_s: str, string_t: str) -> bool:
        """Is anagram?."""
        dict_1, dict_2 = {}, {}
        for char_1 in string_s:
            dict_1[char_1] = dict_1.get(char_1, 0) + 1
        for char_2 in string_t:
            dict_2[char_2] = dict_2.get(char_2, 0) + 1
        return dict_1 == dict_2

    @staticmethod
    def all_cells_dist_order(num_r: int, num_c: int, r_0: int,
                             c_0: int) -> list[[int, int]]:
        """All cells dist order."""
        visited, result = [[False] * num_c for _ in range(num_r)], [[r_0, c_0]]
        visited[r_0][c_0], k = True, 0
        while k < len(result):
            i, j = result[k]
            k += 1
            for i, j in ((i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)):
                if 0 <= i < num_r and 0 <= j < num_c and not visited[i][j]:
                    visited[i][j] = True
                    result.append([i, j])
        return result

    @staticmethod
    def sort_list(head: ListNode) -> ListNode:
        """Sort list."""
        lst, func = [], sorted
        while head:
            lst.append(head.val)
            head = head.next
        lst = func(lst)
        if lst:
            head = ListNode(lst[0])
            node = head
            for elem in lst[1:]:
                node.next = ListNode(elem)
                node = node.next
        return head

    @staticmethod
    def largest_perimeter(array_a: list[int]) -> int:
        """Largest perimeter."""
        func = sorted
        lst = func(array_a, reverse=True)
        for side_1, side_2, side_3 in zip(lst, lst[1:], lst[2:]):
            if side_1 < side_2 + side_3:
                return side_1 + side_2 + side_3
        return 0


def problem_1() -> None:
    """Problem 1."""
    assert Solution.bubble_swap_count([508, 675, 160, 957, 944]) == 3


def problem_2() -> None:
    """Problem 2."""
    array = [250, 38, 664, 852, 900, 418, 484, 694, 940, 546, 929, 775, 957,
             231, 245, 239, 297, 121, 31, 227]
    result = [38, 957, 250, 929, 418, 775, 484, 297, 546, 245, 664, 239, 694,
              231, 852, 227, 900, 121, 940, 31]
    assert Solution.sort_array(array) == result


def problem_3() -> None:
    """Problem 3."""
    assert Solution.is_anagram("deccl", "cledc")


def problem_4() -> None:
    """Problem 4."""
    inp = [3, 3, 2, 1]
    result = [[2, 1], [1, 1], [2, 0], [2, 2], [0, 1], [1, 0], [1, 2], [0, 0],
              [0, 2]]
    assert Solution.all_cells_dist_order(*inp) == result


def create_list(string: str) -> ListNode:
    """Create list."""
    list_gen = map(int, string.split("->"))
    head = ListNode(next(list_gen))
    node = head
    for num in list_gen:
        node.next = ListNode(num)
        node = node.next_node()
    return head


def check(head_1: ListNode, head_2: ListNode) -> None:
    """Check."""
    while head_1 and head_2:
        assert head_1.value() == head_2.value()
        head_1 = head_1.next
        head_2 = head_2.next
    assert head_1 == head_2


def problem_5() -> None:
    """Problem 5."""
    str_1 = "241->805->107->858->753"
    str_2 = "107->241->753->805->858"
    lst_1, lst_2 = create_list(str_1), create_list(str_2)
    check(Solution.sort_list(lst_1), lst_2)


def problem_6() -> None:
    """Problem 6."""
    assert Solution.largest_perimeter([266, 39, 669, 182, 586]) == 1521


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
