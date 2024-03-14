"""Searching tree."""
from typing import Callable

from collections import deque


class TreeNode:
    """TreeNode."""

    def __init__(self, val: int) -> None:
        """Node constructor."""
        self.val = val
        self.left = None
        self.right = None

    def value(self) -> int:
        """Value."""
        return self.val

    def left_right(self) -> ("TreeNode", "TreeNode"):
        """Left, right node."""
        return self.left, self.right


class Solution:
    """Solution."""

    __methods = {"searchBST": "search_binary_search_tree",
                 "lowestCommonAncestor": "lowest_common_ancestor",
                 "maxDepth": "max_depth",
                 "hasPathSum": "has_path_sum",
                 "pathSum": "path_sum"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @staticmethod
    def search_binary_search_tree(head: TreeNode, value: int) -> TreeNode:
        """Search in binary search tree."""
        while head and head.val != value:
            if value < head.val:
                head = head.left
            else:
                head = head.right
        return head

    @staticmethod
    def lowest_common_ancestor(head: TreeNode, node_1: TreeNode,
                               node_2: TreeNode) -> TreeNode:
        """Lowest common ancestor."""
        minimum = min(node_1.val, node_2.val)
        maximum = max(node_1.val, node_2.val)
        while head:
            if head.val < minimum:
                head = head.right
            elif head.val > maximum:
                head = head.left
            else:
                break
        return head

    @classmethod
    def max_depth(cls, head: TreeNode) -> int:
        """Max depth."""
        if not head:
            return 0
        return 1 + max(cls.max_depth(head.left), cls.max_depth(head.right))

    @classmethod
    def diameter(cls, head: TreeNode) -> int:
        """Diameter."""
        if not head:
            return 0
        return cls.max_depth(head.left) + cls.max_depth(head.right)

    @classmethod
    def has_path_sum(cls, head: TreeNode, val: int) -> bool:
        """Has path from root to leaf with sum equal val?."""
        if not head:
            return False
        val -= head.val
        left, right = head.left, head.right
        if not (left or right) and val == 0:
            return True
        return cls.has_path_sum(left, val) or cls.has_path_sum(right, val)

    @classmethod
    def path_sum(cls, head: TreeNode, val: int, take: bool = False) -> int:
        """Count of paths with sum equal val."""
        if not head:
            return 0
        result = 0
        if not take:
            result += cls.path_sum(head.left, val)
            result += cls.path_sum(head.right, val)
        val -= head.val
        result += cls.path_sum(head.left, val, take=True)
        result += cls.path_sum(head.right, val, take=True)
        return result + (val == 0)


def lst_to_tree(lst: list[int]) -> TreeNode:
    """Breadth-first search - BFS."""
    queue, new_head, i, my_dict = deque(), None, 0, {-1: None}
    if lst:
        new_head = my_dict.get(lst[i], TreeNode(lst[i]))
        queue.append(new_head)
        i += 1
    while queue:
        node = queue.popleft()
        if node:
            num_1, num_2 = -1, -1
            if i < len(lst):
                num_1, num_2 = lst[i], lst[i + 1]
                i += 2
            node.left = my_dict.get(num_1, TreeNode(num_1))
            node.right = my_dict.get(num_2, TreeNode(num_2))
            queue.append(node.left)
            queue.append(node.right)
    return new_head


def check(root_1: TreeNode, root_2: TreeNode) -> None:
    """Check."""
    if root_1 and root_2:
        assert root_1.value() == root_2.value()
        left_1, right_1 = root_1.left_right()
        left_2, right_2 = root_2.left_right()
        check(left_1, left_2)
        check(right_1, right_2)
    else:
        assert root_1 == root_2


def problem_1() -> None:
    """Problem 1."""
    lists = [[4, 1, 5], [6, 4, 7, 0, -1, -1, -1]]
    vals = [1, 4]
    results = [[1], [4, 0, -1]]
    heads = list(map(lst_to_tree, lists))
    heads_res = list(map(lst_to_tree, results))
    for i, head in enumerate(heads):
        check(Solution.search_binary_search_tree(head, vals[i]), heads_res[i])


def problem_2() -> None:
    """Problem 2."""
    lst, num_1, num_2 = [1, 0, 5], 5, 0
    result = [1, 0, 5]
    node_1, node_2 = TreeNode(num_1), TreeNode(num_2)
    head = lst_to_tree(lst)
    head_res = lst_to_tree(result)
    check(Solution.lowest_common_ancestor(head, node_1, node_2), head_res)


def problem_3() -> None:
    """Problem 3."""
    lst = [4, 0, 5]
    head = lst_to_tree(lst)
    assert Solution.max_depth(head) == 2


def problem_4() -> None:
    """Problem 4."""
    lst = [2, 0, 4]
    head = lst_to_tree(lst)
    assert Solution.diameter(head) == 2


def problem_5() -> None:
    """Problem 5."""
    lists = [[2, 0, 4], [4, 2, 5, 0, -1, -1, -1],
             [7, 2, 13, 0, 6, 10, -1],
             [17, 10, 28, 5, 15, 21, 29, 1, -1, 11, -1, 20, -1, -1, -1],
             [46, 21, 67, 13, 35, 64, 77, 10, 14, 33, 39, 58, 66, 74, 84, 9,
              -1, -1, -1, 31, -1, -1, -1, 55, -1, -1, -1, -1, -1, -1, -1]]
    vals = [6, 6, 30, 30, 274]
    results = [True, True, True, False, True]
    heads = list(map(lst_to_tree, lists))
    for i, head in enumerate(heads):
        assert Solution.has_path_sum(head, vals[i]) == results[i]


def problem_6() -> None:
    """Problem 6."""
    lst, val = [4, 3, 7, 0, -1, 5, -1], 11
    head = lst_to_tree(lst)
    assert Solution.path_sum(head, val) == 1


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
