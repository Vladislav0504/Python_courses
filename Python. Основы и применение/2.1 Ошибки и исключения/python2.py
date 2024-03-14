"""Errors and exceptions."""
from collections import deque


def search(child: str, exceptions: set[str], edges: dict[str, list[str]],
           visited: dict[str, set[str]]) -> bool:
    """Breadth-first search - BFS."""
    queue = deque([child])
    visited[child].add(child)
    while queue:
        vertex = queue.popleft()
        if vertex in exceptions:
            return True
        for elem in edges[vertex]:
            if elem not in visited[child]:
                queue.append(elem)
                visited[child].add(elem)
    return False


def main():
    """My function."""
    num_n, edges, visited = int(input()), {}, {}
    for _ in range(num_n):
        vertex, *parents = input().split()
        edges[vertex] = parents[1:]
        visited[vertex] = set()
    num_m, exceptions = int(input()), set()
    for _ in range(num_m):
        exception = input()
        if search(exception, exceptions, edges, visited):
            print(exception)
        exceptions.add(exception)


if __name__ == "__main__":
    main()
