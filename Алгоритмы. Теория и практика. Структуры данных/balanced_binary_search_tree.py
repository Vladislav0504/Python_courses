"""Binary search trees.

AVL tree (class BinarySearchTree) with support for methods:
1) insert value;
2) find value;
3) delete value;
4) sum_tree on segment [left, right].
Execution time of these functions is equal O(log n).
Class Node with support for balancing methods:
1) rotate;
2) balance.
In the balance() function first of all big rotations are considered,
and second small rotations.
"""
from sys import stdin, stdout

from typing import Self


class Node:
    """Node."""

    def __init__(self, key: int = None) -> None:
        """Node constructor."""
        self.left, self.right = None, None
        self.key, self.sum = key, key
        self.height = 0

    def rotate(self, child: Self) -> Self:
        """Rotate."""
        if child == self.left:
            self.left = child.right
            child.right = self
        else:
            self.right = child.left
            child.left = self
        for node in (self, child):
            node.sum = node.key + total(node.left) + total(node.right)
            node.height = 1 + max(height(node.left), height(node.right))
        return child

    def balance(self) -> Self:
        """Balance self."""
        h_left, h_right = height(self.left), height(self.right)
        self.sum = self.key + total(self.left) + total(self.right)
        self.height = 1 + max(h_left, h_right)
        if h_left == h_right + 2 == height(self.left.left) + 2:
            self.left = self.left.rotate(self.left.right)
            return self.rotate(self.left)
        if h_right == h_left + 2 == height(self.right.right) + 2:
            self.right = self.right.rotate(self.right.left)
            return self.rotate(self.right)
        if h_left - h_right == 2:
            return self.rotate(self.left)
        if h_right - h_left == 2:
            return self.rotate(self.right)
        return self


def height(node: Node) -> int:
    """Node height."""
    return node.height if node else -1


def total(node: Node) -> int:
    """Node sum."""
    return node.sum if node else 0


def search_first(node: Node, left: int, right: int) -> Node:
    """Search first node: left <= node.key <= right."""
    while node:
        if left <= node.key <= right:
            return node
        if node.key < left:
            node = node.right
        else:
            node = node.left
    return node


class BinarySearchTree:
    """BinarySearchTree."""

    root = None

    def insert(self, node: Node, value: int) -> Node:
        """Insert value."""
        if not node:
            return Node(value)
        if value < node.key:
            node.left = self.insert(node.left, value)
        elif value > node.key:
            node.right = self.insert(node.right, value)
        return node.balance()

    def find(self, value: int) -> int:
        """Find value."""
        node = search_first(self.root, value, value)
        return stdout.write("Found\n" if node else "Not found\n")

    def delete(self, node: Node, value: int) -> Node:
        """Delete value."""
        if not node:
            return node
        if value == node.key:
            if node.right:
                node_min = node.right
                while node_min.left:
                    node_min = node_min.left
                node.key = node_min.key
                node.right = self.delete(node.right, node.key)
            else:
                return node.left
        elif value < node.key:
            node.left = self.delete(node.left, value)
        else:
            node.right = self.delete(node.right, value)
        return node.balance()

    def sum_tree(self, left: int, right: int) -> int:
        """Total on segment [left, right]."""
        node = search_first(self.root, left, right)
        result = total(node)
        borders = ((node, "left", "right"), (node, "right", "left"))
        for vertex, arg_1, arg_2 in borders:
            while vertex:
                if vertex.key < left or vertex.key > right:
                    result -= vertex.key + total(getattr(vertex, arg_1))
                    vertex = getattr(vertex, arg_2)
                else:
                    vertex = getattr(vertex, arg_1)
        return result


def func(num_x: str, num_s: int) -> int:
    """Additional function."""
    mod = 1000000001
    return (int(num_x) + num_s) % mod


def main():
    """My function."""
    reader, tree = (line.split() for line in stdin), BinarySearchTree()
    num_s, _ = 0, next(reader)
    for operation, *nums in reader:
        if operation == "+":
            tree.root = tree.insert(tree.root, func(nums[0], num_s))
        elif operation == "-":
            tree.root = tree.delete(tree.root, func(nums[0], num_s))
        elif operation == "?":
            tree.find(func(nums[0], num_s))
        else:
            num_s = tree.sum_tree(func(nums[0], num_s), func(nums[1], num_s))
            stdout.write(f"{num_s}\n")


if __name__ == "__main__":
    main()
