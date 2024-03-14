"""Classes."""
from collections import deque


def search(child: str, edges: dict[str, list[str]],
           ancestors: dict[str, set[str]]) -> None:
    """Breadth-first search - BFS."""
    queue = deque([child])
    ancestors[child].add(child)
    while queue:
        vertex = queue.popleft()
        for elem in edges[vertex]:
            if elem not in ancestors[child]:
                queue.append(elem)
                ancestors[child].add(elem)


def main():
    """My function."""
    num_n, edges, ancestors = int(input()), {}, {}
    answers = ("No", "Yes")
    for _ in range(num_n):
        vertex, *parents = input().split()
        edges[vertex] = parents[1:]
        ancestors[vertex] = set()
    num_q = int(input())
    for _ in range(num_q):
        ancestor, child = input().split()
        if not ancestors[child]:
            search(child, edges, ancestors)
        print(answers[ancestor in ancestors[child]])


if __name__ == "__main__":
    main()
