"""Basic data structures."""


def main():
    """My function."""
    num_n = int(input())
    tree = tuple([] for _ in range(num_n + 1))
    for i, parent in enumerate(map(int, input().split())):
        tree[parent].append(i)
    height, stack = 0, [tree[-1][0]]
    start, end = 0, 1
    while start < end:
        for vertex in stack[start:]:
            stack.extend(tree[vertex])
        start, end = end, len(stack)
        height += 1
    print(height)


if __name__ == "__main__":
    main()
