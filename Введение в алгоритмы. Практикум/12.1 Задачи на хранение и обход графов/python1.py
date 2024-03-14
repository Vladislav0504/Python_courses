"""Graph traversal."""
from typing import Callable


def search(vertex: int, visited: list[int], edges: list[list[int]]) -> bool:
    """Depth-first search - DFS."""
    visited[vertex] = -1
    for elem in edges[vertex]:
        if (visited[elem] == -1 or
                visited[elem] == 0 and not search(elem, visited, edges)):
            return False
    visited[vertex] = 1
    return True


class Solution:
    """Solution."""

    __methods = {"canVisitAllRooms": "can_visit_all_rooms",
                 "canFinish": "can_finish",
                 "isBipartite": "is_bipartite",
                 "canReach": "can_reach"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @staticmethod
    def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
        """Can visit all rooms?."""
        visited, i = [False] * len(rooms), 0
        queue, visited[0] = [0], True
        while i < len(queue):
            room = queue[i]
            i += 1
            for k in rooms[room]:
                if not visited[k]:
                    queue.append(k)
                    visited[k] = True
        return all(visited)

    @staticmethod
    def can_finish(num: int, prerequisites: list[[int, int]]) -> bool:
        """Can finish?."""
        visited, edges = [0] * num, [[] for _ in range(num)]
        for course_i, requirement in prerequisites:
            edges[course_i].append(requirement)
        for course, state in enumerate(visited):
            if state == 0 and not search(course, visited, edges):
                return False
        return True

    @staticmethod
    def is_bipartite(graph: list[list[int]]) -> bool:
        """Is bipartite?."""
        visited, queue, i = [0] * len(graph), [], 0
        for j, state in enumerate(visited):
            if state == 0:
                visited[j] = 1
                queue.append(j)
                while i < len(queue):
                    vertex = queue[i]
                    i += 1
                    for k in graph[vertex]:
                        if visited[k] == 0:
                            queue.append(k)
                            visited[k] = -visited[vertex]
                        elif visited[k] == visited[vertex]:
                            return False
        return True

    @staticmethod
    def can_reach(arr: list[int], start: int) -> bool:
        """Can reach any zeros in arr?."""
        if arr[start] == 0:
            return True
        length = len(arr)
        visited, i = [False] * length, 0
        queue, visited[start] = [start], True
        while i < len(queue):
            index = queue[i]
            i += 1
            for k in (index - arr[index], index + arr[index]):
                if 0 <= k < length and not visited[k]:
                    queue.append(k)
                    visited[k] = True
                    if arr[k] == 0:
                        return True
        return False

    @staticmethod
    def jump(arr: list[int]) -> int:
        """Minimum number of jumps from start to end of arr."""
        jumps = [len(arr)] * len(arr)
        jumps[0], min_step = 0, 0
        for i, elem in enumerate(arr):
            for j in range(min_step, elem + 1):
                if i + j < len(arr) and jumps[i + j] > jumps[i] + 1:
                    jumps[i + j] = jumps[i] + 1
            min_step = max(min_step - 1, elem)
        return jumps[-1]


def problem_1() -> None:
    """Problem 1."""
    tests = [[[1], [2], [3], []], [[1, 3], [3, 0, 1], [2], [0]]]
    results = [True, False]
    for test, result in zip(tests, results):
        assert Solution.can_visit_all_rooms(test) == result


def problem_2() -> None:
    """Problem 2."""
    tests = [(2, [[1, 0]]), (2, [[1, 0], [0, 1]])]
    results = [True, False]
    for test, result in zip(tests, results):
        assert Solution.can_finish(*test) == result


def problem_3() -> None:
    """Problem 3."""
    tests = [[[1, 3], [0, 2], [1, 3], [0, 2]],
             [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]]
    results = [True, False]
    for test, result in zip(tests, results):
        assert Solution.is_bipartite(test) == result


def problem_4() -> None:
    """Problem 4."""
    tests = [([4, 2, 3, 0, 3, 1, 2], 5), ([3, 0, 2, 1, 2], 2)]
    results = [True, False]
    for test, result in zip(tests, results):
        assert Solution.can_reach(*test) == result


def problem_5() -> None:
    """Problem 5."""
    test, result = [2, 3, 1, 1, 4], 2
    assert Solution.jump(test) == result


def main():
    """My function."""
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()


if __name__ == "__main__":
    main()
