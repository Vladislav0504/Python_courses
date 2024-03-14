"""Network maxflow."""
from sys import stdin


def search(cur_v: int, end: int, delta: int, visited: list[bool],
           edges: list[dict[int, int]]) -> int:
    """Depth-first search - DFS."""
    if cur_v == end:
        return delta
    visited[cur_v] = True
    for next_v, capacity in edges[cur_v].items():
        if not visited[next_v] and capacity:
            delta_1 = search(next_v, end, min(delta, capacity), visited, edges)
            if delta_1:
                edges[cur_v][next_v] -= delta_1
                edges[next_v][cur_v] += delta_1
                return delta_1
    return 0


def main():
    """My function."""
    reader = (map(int, line.split()) for line in stdin)
    count_v, _ = next(reader)
    edges = [{} for _ in range(count_v)]
    for u_i, v_i, c_i in reader:
        if u_i != v_i:
            edges[u_i][v_i] = edges[u_i].get(v_i, 0) + c_i
            edges[v_i][u_i] = edges[v_i].get(u_i, 0)
    max_flow, delta, maximum = 0, 1, 50
    while delta:
        delta = search(0, count_v - 1, maximum, [False] * count_v, edges)
        max_flow += delta
    print(max_flow)


if __name__ == "__main__":
    main()
