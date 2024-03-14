"""List."""
from typing import Callable


class ListNode:
    """ListNode."""

    def __init__(self, val: int) -> None:
        """Node constructor."""
        self.val = val
        self.next = None
        self.prev = None

    def value(self) -> int:
        """Value."""
        return self.val

    def next_prev(self) -> ("ListNode", "ListNode"):
        """Next, prev."""
        return self.next, self.prev


class Solution:
    """Solution."""

    __methods = {"isPalindrome": "is_palindrome",
                 "reorderList": "reorder_list"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @staticmethod
    def is_palindrome(head_list: ListNode, tail_list: ListNode) -> bool:
        """Is palindrome?."""
        while head_list != tail_list and head_list.val == tail_list.val:
            head_list = head_list.next
            tail_list = tail_list.prev
        return head_list == tail_list

    @staticmethod
    def reorder_list(head_list: ListNode, tail_list: ListNode) -> ListNode:
        """Reorder list."""
        head_0, tail_0 = head_list, tail_list
        while tail_0 not in (head_0, head_0.next):
            node_1, node_2 = head_0.next, tail_0.prev
            head_0.next, tail_0.prev = tail_0, head_0
            tail_0.next, node_1.prev = node_1, tail_0
            node_2.next = None
            head_0, tail_0 = node_1, node_2
        return head_list


def create_list(string: str) -> (ListNode, ListNode):
    """Create list."""
    my_list = list(map(int, string.split("<->")))
    head = ListNode(my_list[0])
    node, prev = head, None
    for num in my_list[1:]:
        node.next, node.prev = ListNode(num), prev
        node, prev = node.next_prev()[0], node
    node.prev = prev
    tail = node
    return head, tail


def check(head_1: ListNode, head_2: ListNode,
          tail_1: ListNode, tail_2: ListNode) -> None:
    """Check."""
    while head_1 and head_2:
        assert head_1.val == head_2.val
        head_1 = head_1.next
        head_2 = head_2.next
    assert head_1 == head_2
    while tail_1 and tail_2:
        assert tail_1.val == tail_2.val
        tail_1 = tail_1.prev
        tail_2 = tail_2.prev
    assert tail_1 == tail_2


def problem_1() -> None:
    """Problem 1."""
    str_1 = "2<->1<->8<->18<->6<->1<->13<->8<->11<->10<->12<->"
    str_2 = "8<->19<->14<->13<->15<->4<->3<->15<->15"
    my_list = "".join((str_1, str_2))
    head, tail = create_list(my_list)
    result = False
    assert head.value() == 2
    assert Solution.is_palindrome(head, tail) == result


def problem_2() -> None:
    """Problem 2."""
    str_1 = "3<->12<->2<->10<->12<->5<->3<->6<->1<->14<->"
    str_2 = "14<->18<->11<->6<->8<->17<->20<->1<->14<->9"
    list_1 = "".join((str_1, str_2))
    str_1 = "3<->9<->12<->14<->2<->1<->10<->20<->12<->17<->"
    str_2 = "5<->8<->3<->6<->6<->11<->1<->18<->14<->14"
    list_2 = "".join((str_1, str_2))
    head_1, tail_1 = create_list(list_1)
    head_2, tail_2 = create_list(list_2)
    res_head = Solution.reorder_list(head_1, tail_1)
    res_tail = res_head
    while res_tail.next:
        res_tail = res_tail.next
    check(res_head, head_2, res_tail, tail_2)


def main():
    """My function."""
    problem_1()
    problem_2()


if __name__ == "__main__":
    main()
