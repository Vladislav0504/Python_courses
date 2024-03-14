"""Binary search trees."""
from sys import stdin, stdout


def in_order(vertex: (int, int, int), tree: list[(int, int, int)]) -> None:
    """In-order."""
    key, left, right = vertex
    if left != -1:
        in_order(tree[left], tree)
    stdout.write(f"{key} ")
    if right != -1:
        in_order(tree[right], tree)


def pre_order(vertex: (int, int, int), tree: list[(int, int, int)]) -> None:
    """Pre-order."""
    key, left, right = vertex
    stdout.write(f"{key} ")
    if left != -1:
        pre_order(tree[left], tree)
    if right != -1:
        pre_order(tree[right], tree)


def post_order(vertex: (int, int, int), tree: list[(int, int, int)]) -> None:
    """Post-order."""
    key, left, right = vertex
    if left != -1:
        post_order(tree[left], tree)
    if right != -1:
        post_order(tree[right], tree)
    stdout.write(f"{key} ")


def main():
    """My function."""
    reader = (tuple(map(int, line.split())) for line in stdin)
    next(reader)
    tree = list(reader)
    in_order(tree[0], tree)
    stdout.write("\n")
    pre_order(tree[0], tree)
    stdout.write("\n")
    post_order(tree[0], tree)


if __name__ == "__main__":
    main()
