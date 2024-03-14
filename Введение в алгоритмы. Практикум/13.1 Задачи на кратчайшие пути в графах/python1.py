"""Shortest paths in graphs."""
from typing import Callable

from collections import deque


def legal_points(func: Callable[[int, int], bool], coord: (int, int),
                 box: bool = False) -> list[(int, int)]:
    """Next legal coordinates."""
    result = []
    for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        new_coord = (coord[0] + i, coord[1] + j)
        if func(*new_coord) and (not box or func(coord[0] - i, coord[1] - j)):
            result.append(new_coord)
    return result


def search(coord_s: (int, int), coord_b: (int, int),
           func: Callable[[int, int], bool]) -> list[(int, int)]:
    """Breadth-first search - BFS."""
    queue, visited, result = deque([coord_s]), {coord_s}, []
    ends = legal_points(func, coord_b, True)
    while queue:
        vertex = queue.popleft()
        if vertex in ends:
            result.append(vertex)
        for coord in legal_points(func, vertex):
            if coord != coord_b and coord not in visited:
                visited.add(coord)
                queue.append(coord)
    return result


class Solution:
    """Solution."""

    __methods = {"shortestPathLength": "shortest_path_length",
                 "shortestAlternatingPaths": "shortest_alternating_paths",
                 "shortestPathBinaryMatrix": "shortest_path_binary_matrix",
                 "minPushBox": "min_push_box"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @staticmethod
    def shortest_path_length(graph: list[list[int]]) -> int:
        """Shortest path length."""
        num_n = len(graph)
        total = (1 << num_n) - 1
        queue = deque([(1 << i, i) for i in range(num_n)])
        dist = [[-1] * num_n for _ in range(1 << num_n)]
        for i in range(num_n):
            dist[1 << i][i] = 0
        while queue:
            visited, vertex = queue.popleft()
            for j in graph[vertex]:
                new_visited = visited | 1 << j
                if dist[new_visited][j] == -1:
                    dist[new_visited][j] = dist[visited][vertex] + 1
                    queue.append((new_visited, j))
                if new_visited == total:
                    return dist[new_visited][j]
        return 0

    @staticmethod
    def shortest_alternating_paths(num_n: int, red_edges: list[[int, int]],
                                   blue_edges: list[[int, int]]) -> list[int]:
        """Shortest alternating paths."""
        edges = [([], []) for _ in range(max(num_n, 1))]
        for red_0, red_1 in red_edges:
            edges[red_0][0].append(red_1)
        for blue_0, blue_1 in blue_edges:
            edges[blue_0][1].append(blue_1)
        queue, result = deque([(0, 0), (0, 1)]), [-1] * num_n
        depth = [[-1, -1] for _ in range(num_n)]
        depth[:1], result[:1] = [[0, 0]], [0] * min(num_n, 1)
        while queue:
            vertex, color = queue.popleft()
            for next_vertex in edges[vertex][color]:
                color_2 = 1 - color
                if depth[next_vertex][color_2] == -1:
                    depth[next_vertex][color_2] = depth[vertex][color] + 1
                    if (result[next_vertex] == -1 or
                            depth[next_vertex][color_2] < result[next_vertex]):
                        result[next_vertex] = depth[next_vertex][color_2]
                    queue.append((next_vertex, color_2))
        return result

    @staticmethod
    def shortest_path_binary_matrix(grid: list[list[int]]) -> int:
        """Shortest path binary matrix."""
        num_n = len(grid)
        if num_n == 0 or grid[0][0] and num_n != 1:
            return -1
        queue, depth = deque([(0, 0)]), {(0, 0): 1}
        while queue:
            coord_0, coord_1 = queue.popleft()
            if coord_0 == coord_1 == num_n - 1:
                return depth[coord_0, coord_1]
            for i in range(max(0, coord_0 - 1), min(num_n, coord_0 + 2)):
                for j in range(max(0, coord_1 - 1), min(num_n, coord_1 + 2)):
                    if (i, j) not in depth and grid[i][j] == 0:
                        depth[i, j] = depth[coord_0, coord_1] + 1
                        queue.append((i, j))
        return -1

    @staticmethod
    def min_push_box(grid: list[list[str]]) -> int:
        """Min push box."""
        coord = {}
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value in "SB":
                    coord[value] = (i, j)
        queue = deque([(coord["S"], coord["B"])])
        depth = {queue[0]: 0}
        while queue:
            coord_s, coord_b = queue.popleft()
            for k_0, k_1 in search(coord_s, coord_b,
                                   lambda x, y: (0 <= x < len(grid) and
                                                 0 <= y < len(grid[0]) and
                                                 grid[x][y] != "#")):
                coord_b_2 = ((coord_b[0] << 1) - k_0, (coord_b[1] << 1) - k_1)
                new_coord = (coord_b, coord_b_2)
                if new_coord not in depth:
                    depth[new_coord] = depth[(coord_s, coord_b)] + 1
                    queue.append(new_coord)
                    if grid[coord_b_2[0]][coord_b_2[1]] == "T":
                        return depth[new_coord]
        return -1


def problem_1() -> None:
    """Problem 1."""
    tests = [[[1, 2, 3], [0], [0], [0]],
             [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]]
    results = [4, 4]
    for test, result in zip(tests, results):
        assert Solution.shortest_path_length(test) == result


def problem_2() -> None:
    """Problem 2."""
    tests = [(3, [[0, 1], [1, 2]], []), (3, [[0, 1]], [[2, 1]]),
             (3, [[1, 0]], [[2, 1]])]
    results = [[0, 1, -1], [0, 1, -1], [0, -1, -1]]
    for test, result in zip(tests, results):
        assert Solution.shortest_alternating_paths(*test) == result


def problem_3() -> None:
    """Problem 3."""
    tests = [[[0, 1], [1, 0]], [[0, 0, 0], [1, 1, 0], [1, 1, 0]],
             [[1, 0, 0], [1, 1, 0], [1, 1, 0]]]
    results = [2, 4, -1]
    for test, result in zip(tests, results):
        assert Solution.shortest_path_binary_matrix(test) == result


def problem_4() -> None:
    """Problem 4."""
    tests = [[["#", "#", "#", "#", "#", "#"],
              ["#", "T", "#", "#", "#", "#"],
              ["#", ".", ".", "B", ".", "#"],
              ["#", ".", "#", "#", ".", "#"],
              ["#", ".", ".", ".", "S", "#"],
              ["#", "#", "#", "#", "#", "#"]],
             [["#", "#", "#", "#", "#", "#"],
              ["#", "T", "#", "#", "#", "#"],
              ["#", ".", ".", "B", ".", "#"],
              ["#", "#", "#", "#", ".", "#"],
              ["#", ".", ".", ".", "S", "#"],
              ["#", "#", "#", "#", "#", "#"]],
             [["#", "#", "#", "#", "#", "#"],
              ["#", "T", ".", ".", "#", "#"],
              ["#", ".", "#", "B", ".", "#"],
              ["#", ".", ".", ".", ".", "#"],
              ["#", ".", ".", ".", "S", "#"],
              ["#", "#", "#", "#", "#", "#"]]]
    results = [3, -1, 5]
    for test, result in zip(tests, results):
        assert Solution.min_push_box(test) == result


def main():
    """My function."""
    problem_1()
    problem_2()
    problem_3()
    problem_4()


if __name__ == "__main__":
    main()
