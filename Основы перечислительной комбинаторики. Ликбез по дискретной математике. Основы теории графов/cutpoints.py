"""Cutpoints."""
import sys

RECURSION_LIMIT, SYS_ATTR = 8000, "setrecursionlimit"
getattr(sys, SYS_ATTR)(RECURSION_LIMIT)


def cut_points(cur: int, edges: dict[int, set[int]], time_in: list[int],
               result: set[int]) -> int:
    """Depth-first search - DFS."""
    children, time_up_cur = 0, time_in[cur]
    for child in edges[cur]:
        if 0 <= time_in[child] < time_up_cur:
            time_up_cur = time_in[child]
        if time_in[child] == -1:
            children += 1
            edges[child].remove(cur)
            time_in[child] = time_in[cur] + 1
            time_up_child = cut_points(child, edges, time_in, result)
            time_up_cur = min(time_up_cur, time_up_child)
            if 0 < time_in[cur] <= time_up_child:
                result.add(cur)
    if time_in[cur] == 0 and children > 1:
        result.add(cur)
    return time_up_cur


def main():
    """My function."""
    reader = (map(int, line.split()) for line in sys.stdin)
    edges, result, start = {}, set(), 0
    for vertex_1, vertex_2 in reader:
        edges.setdefault(vertex_1, set()).add(vertex_2)
        edges.setdefault(vertex_2, set()).add(vertex_1)
    time_in = [-1] * len(edges)
    time_in[start] = 0
    cut_points(start, edges, time_in, result)
    print(*result)


if __name__ == "__main__":
    main()
