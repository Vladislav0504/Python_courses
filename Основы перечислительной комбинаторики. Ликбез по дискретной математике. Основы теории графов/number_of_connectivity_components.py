"""Number of connectivity components."""
from sys import stdin


def search(vertex: int, visited: list[bool], edges: list[list[int]]) -> None:
    """Depth-first search - DFS."""
    visited[vertex] = True
    for elem in edges[vertex]:
        if not visited[elem]:
            search(elem, visited, edges)


def main():
    """My function."""
    reader = (map(int, line.split()) for line in stdin)
    count_v, _ = next(reader)
    edges = [[] for _ in range(count_v + 1)]
    visited = [False] * (count_v + 1)
    for vertex_1, vertex_2 in reader:
        edges[vertex_1].append(vertex_2)
        edges[vertex_2].append(vertex_1)
    print(sum(0 if visited[v] else search(v, visited, edges) is None
              for v in range(1, count_v + 1)))


if __name__ == "__main__":
    main()
