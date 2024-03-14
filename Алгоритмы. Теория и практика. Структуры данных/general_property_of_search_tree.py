"""Binary search trees."""
from sys import stdin

from collections import deque


def is_correct(tree: list[(int, int, int)]) -> bool:
    """Is binary tree correct?."""
    degree = 31
    queue, limit = deque(), 1 << degree
    if tree:
        queue.append((tree[0], -limit, limit))
    while queue:
        vertex, key_left, key_right = queue.popleft()
        key, left, right = vertex
        if key >= key_right or key < key_left:
            return False
        if left != -1:
            queue.append((tree[left], key_left, key))
        if right != -1:
            queue.append((tree[right], key, key_right))
    return True


def main():
    """My function."""
    reader = (tuple(map(int, line.split())) for line in stdin)
    next(reader)
    tree = list(reader)
    print("CORRECT" if is_correct(tree) else "INCORRECT")


if __name__ == "__main__":
    main()
