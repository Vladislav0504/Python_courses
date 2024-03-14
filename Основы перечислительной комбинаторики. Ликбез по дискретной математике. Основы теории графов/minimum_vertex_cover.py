"""Minimum vertex cover.

Good program.
"""
from sys import stdin, stdout


def search(cur_v: int, visited: list[bool], edges: list[list[int]]) -> bool:
    """Depth-first search - DFS."""
    if visited[cur_v]:
        return False
    visited[cur_v] = True
    for next_v in edges[cur_v]:
        if edges[next_v][0] < 0 or search(edges[next_v][0], visited, edges):
            edges[next_v][0] = cur_v
            return True
    return False


def main():
    """My function."""
    reader = (map(int, line.split()) for line in stdin)
    v_1, v_2, count_e = next(reader)
    stdout.write(f"{v_1} {v_2} {count_e}\n")
    edges = [[] for _ in range(v_1)] + [[-1] for _ in range(v_2)]
    for u_i, w_i in reader:
        edges[u_i].append(w_i)
        stdout.write(f"{u_i} {w_i}\n")
    for v_i in range(v_1):
        search(v_i, [False] * v_1, edges)
    unsaturated = set(range(v_1)).difference({u_1[0] for u_1 in edges[v_1:]})
    visited = [False] * v_1
    for v_j in unsaturated:
        search(v_j, visited, edges)
    result = {u_1 for u_1 in range(v_1) if not visited[u_1]}
    result |= {u_2 for u_2, u_1 in enumerate(edges[v_1:], v_1)
               if u_1[0] >= 0 and u_1[0] not in result}
    print(*result)


if __name__ == "__main__":
    main()
