"""Distances in graph."""
from sys import stdin

from collections import deque


def search(start: int, edges: list[list[int]]) -> list[int]:
    """Breadth-first search - BFS."""
    queue, dist = deque([start]), [-1] * len(edges)
    dist[start] = 0
    while queue:
        vertex = queue.popleft()
        for elem in edges[vertex]:
            if dist[elem] == -1:
                dist[elem] = dist[vertex] + 1
                queue.append(elem)
    return dist


def main():
    """My function."""
    reader = (map(int, line.split()) for line in stdin)
    count_v, _ = next(reader)
    edges = [[] for _ in range(count_v)]
    for vertex_1, vertex_2 in reader:
        edges[vertex_1].append(vertex_2)
        edges[vertex_2].append(vertex_1)
    print(*search(0, edges))


if __name__ == "__main__":
    main()
