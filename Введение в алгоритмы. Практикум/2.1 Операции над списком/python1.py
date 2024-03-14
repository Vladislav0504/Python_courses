"""List."""
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

    __methods = {"getDecimalValue": "get_decimal_value",
                 "deleteDuplicates": "delete_duplicates",
                 "insertIntoSorted": "insert_into_sorted"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @staticmethod
    def get_decimal_value(head_list: ListNode) -> int:
        """Get decimal value."""
        result = 0
        while head_list:
            result <<= 1
            result += head_list.val
            head_list = head_list.next
        return result

    @staticmethod
    def delete_duplicates(head_list: ListNode) -> ListNode:
        """Delete duplicates."""
        node = head_list
        while node:
            if node.next and node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next
        return head_list

    @staticmethod
    def insert_into_sorted(head_list: ListNode, value: int) -> ListNode:
        """Insert into sorted."""
        node = head_list
        if not node or node.val <= value:
            head_list = ListNode(value)
            head_list.next = node
        else:
            while node.next and node.next.val > value:
                node = node.next
            cur = ListNode(value)
            cur.next = node.next
            node.next = cur
        return head_list

    @staticmethod
    def reverse(head_list: ListNode) -> ListNode:
        """Reverse."""
        prev = None
        while head_list:
            temp, head_list.next = head_list.next, prev
            prev, head_list = head_list, temp
        return prev


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
        assert head_1.val == head_2.val
        head_1 = head_1.next
        head_2 = head_2.next
    assert head_1 == head_2


def problem_1() -> None:
    """Problem 1."""
    str_1 = "1->1->0->1->0->1->0->1->0->1->1->1->"
    str_2 = "0->0->1->0->1->0->0->1->0->1->1->0"
    my_list = "".join((str_1, str_2))
    head = create_list(my_list)
    result = 13988502
    assert head.value() == 1
    assert Solution.get_decimal_value(head) == result


def problem_2() -> None:
    """Problem 2."""
    list_1 = "1->4->6->7->9->9->10->11->14->14"
    list_2 = "1->4->6->7->9->10->11->14"
    head_1 = create_list(list_1)
    head_2 = create_list(list_2)
    result = Solution.delete_duplicates(head_1)
    check(result, head_2)


def problem_3() -> None:
    """Problem 3."""
    str_1 = "20->15->15->14->13->13->13->11->"
    str_2 = "9->7->7->6->6->4->4->4->3->3->1->1"
    list_1 = "".join((str_1, str_2))
    value = 6
    str_2 = "9->7->7->6->6->6->4->4->4->3->3->1->1"
    list_2 = "".join((str_1, str_2))
    head_1 = create_list(list_1)
    head_2 = create_list(list_2)
    result = Solution.insert_into_sorted(head_1, value)
    check(result, head_2)


def problem_4() -> None:
    """Problem 4."""
    str_1 = "19->20->8->20->16->8->16->1->2->2->"
    str_2 = "8->15->17->13->18->7->5->10->4->16"
    list_1 = "".join((str_1, str_2))
    str_1 = "16->4->10->5->7->18->13->17->15->8->"
    str_2 = "2->2->1->16->8->16->20->8->20->19"
    list_2 = "".join((str_1, str_2))
    head_1 = create_list(list_1)
    head_2 = create_list(list_2)
    result = Solution.reverse(head_1)
    check(result, head_2)


def main():
    """My function."""
    problem_1()
    problem_2()
    problem_3()
    problem_4()


if __name__ == "__main__":
    main()
