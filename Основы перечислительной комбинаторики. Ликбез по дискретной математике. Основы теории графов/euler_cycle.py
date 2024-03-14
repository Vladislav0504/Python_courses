"""Euler cycle."""
from sys import stdin


def euler_cycle(vertex: int, first_edge: list[int], visited: list[bool],
                edges: list[list[[int, int]]], result: list[int]) -> list[int]:
    """Euler cycle."""
    while first_edge[vertex] < len(edges[vertex]):
        i, new_v = edges[vertex][first_edge[vertex]]
        first_edge[vertex] += 1
        if not visited[i]:
            visited[i] = True
            euler_cycle(new_v, first_edge, visited, edges, result)
            result.append(vertex)
    return result


def main():
    """My function."""
    reader = (map(int, line.split()) for line in stdin)
    count_v, _ = next(reader)
    edges, visited = [[] for _ in range(count_v + 1)], []
    for i, (vertex_1, vertex_2) in enumerate(reader):
        visited.append(False)
        edges[vertex_1].append([i, vertex_2])
        edges[vertex_2].append([i, vertex_1])
    if any(map(lambda x: len(x) & 1 or not x, edges[1:])):
        print("NONE")
        return
    result = euler_cycle(1, [0] * len(edges), visited, edges, [])
    if len(set(result)) == count_v:
        print(*result)
    else:
        print("NONE")


if __name__ == "__main__":
    main()
