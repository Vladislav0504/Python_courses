"""Bipartite graph."""
from sys import stdin

from collections import deque


def is_bipartite(cur_v: int, color: list[int], edges: list[list[int]]) -> bool:
    """Is bipartite?."""
    queue, color[cur_v] = deque([cur_v]), 1
    while queue:
        vertex = queue.popleft()
        for next_vertex in edges[vertex]:
            if color[next_vertex] == 0:
                color[next_vertex] = -color[vertex]
                queue.append(next_vertex)
            elif color[next_vertex] == color[vertex]:
                return False
    return True


def main():
    """My function."""
    reader = (map(int, line.split()) for line in stdin)
    count_v, _ = next(reader)
    edges, color = [[] for _ in range(count_v + 1)], [0] * (count_v + 1)
    for v_1, v_2 in reader:
        edges[v_1].append(v_2)
        edges[v_2].append(v_1)
    for v_i, part in enumerate(color):
        if part == 0 and not is_bipartite(v_i, color, edges):
            print("NO")
            break
    else:
        print("YES")


if __name__ == "__main__":
    main()
