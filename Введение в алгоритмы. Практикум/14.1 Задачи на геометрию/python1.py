"""Geometry."""
from typing import Callable


class Solution:
    """Solution."""

    __methods = {"minTimeToVisitAllPoints": "min_time_to_visit_all_points",
                 "surfaceArea": "surface_area",
                 "checkStraightLine": "check_straight_line",
                 "minAreaFreeRect": "min_area_free_rect",
                 "checkOverlap": "check_overlap"}

    def __getattr__(self, attr: str) -> Callable:
        """Attribute correction."""
        return getattr(self, self.__methods[attr])

    @staticmethod
    def min_time_to_visit_all_points(points: list[[int, int]]) -> int:
        """Min time to visit all points."""
        return sum(max(abs(x_1 - x_2), abs(y_1 - y_2))
                   for (x_1, y_1), (x_2, y_2) in zip(points, points[1:]))

    @staticmethod
    def surface_area(grid: list[list[int]]) -> int:
        """Surface area."""
        ans = sum(sum(row) for row in grid) << 2
        grid.extend([[0] * (len(grid))])
        for i, row in enumerate(grid):
            row.append(0)
            for j, k in enumerate(row):
                if k > 0:
                    ans += 1 - min(k, row[j + 1]) - min(k, grid[i + 1][j]) << 1
        return ans

    @staticmethod
    def check_straight_line(coordinates: list[[int, int]]) -> bool:
        """Check straight line."""
        coordinates = list(set(tuple(point) for point in coordinates))
        if len(coordinates) <= 2:
            return True
        (x_1, y_1), (x_2, y_2) = coordinates[0], coordinates[1]
        diff_x, diff_y = x_2 - x_1, y_2 - y_1
        for coord_x, coord_y in coordinates[2:]:
            if (coord_x - x_1) * diff_y != (coord_y - y_1) * diff_x:
                return False
        return True

    @staticmethod
    def min_area_free_rect(points: list[[int, int]]) -> float:
        """Min area free rectangle."""
        my_set = set(tuple(point) for point in points)
        area, points = None, list(my_set)
        area_2 = area
        for i, (x_1, y_1) in enumerate(points):
            for j, (x_2, y_2) in enumerate(points[i + 1:], i + 1):
                sq_21 = (x_2 - x_1)**2 + (y_2 - y_1)**2
                for x_3, y_3 in points[j + 1:]:
                    sq_31 = (x_3 - x_1)**2 + (y_3 - y_1)**2
                    sq_32 = (x_3 - x_2)**2 + (y_3 - y_2)**2
                    if (sq_21 + sq_31 == sq_32 and
                            (x_3 + x_2 - x_1, y_3 + y_2 - y_1) in my_set):
                        area_2 = sq_21 * sq_31
                    elif (sq_21 + sq_32 == sq_31 and
                          (x_1 + x_3 - x_2, y_1 + y_3 - y_2) in my_set):
                        area_2 = sq_21 * sq_32
                    elif (sq_32 + sq_31 == sq_21 and
                          (x_2 + x_1 - x_3, y_2 + y_1 - y_3) in my_set):
                        area_2 = sq_31 * sq_32
                    if not area or area_2 < area:
                        area = area_2
        return (area or 0)**0.5

    @staticmethod
    def check_overlap(radius: int, x_c: int, y_c: int,
                      *rectangle: int) -> bool:
        """Check overlap."""
        x_1, y_1, x_2, y_2 = rectangle
        x_c1, y_c1, x_c2, y_c2 = x_c - x_1, y_c - y_1, x_c - x_2, y_c - y_2
        condition_1 = min(x_c1**2 + y_c1**2, x_c1**2 + y_c2**2,
                          x_c2**2 + y_c1**2, x_c2**2 + y_c2**2) <= radius**2
        condition_2 = max(x_c2, -x_c1) <= radius and y_c2 <= 0 <= y_c1
        condition_3 = x_c2 <= 0 <= x_c1 and max(y_c2, -y_c1) <= radius
        return condition_1 or condition_2 or condition_3


def problem_1() -> None:
    """Problem 1."""
    tests = [[[1, 1], [3, 4], [-1, 0]], [[3, 2], [-2, 2]]]
    results = [7, 5]
    for test, result in zip(tests, results):
        assert Solution.min_time_to_visit_all_points(test) == result


def problem_2() -> None:
    """Problem 2."""
    tests = [[[2]], [[1, 2], [3, 4]], [[1, 0], [0, 2]]]
    results = [10, 34, 16]
    for test, result in zip(tests, results):
        assert Solution.surface_area(test) == result


def problem_3() -> None:
    """Problem 3."""
    tests = [[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]],
             [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]]
    results = [True, False]
    for test, result in zip(tests, results):
        assert Solution.check_straight_line(test) == result


def problem_4() -> None:
    """Problem 4."""
    tests = [[[1, 2], [2, 1], [1, 0], [0, 1]],
             [[0, 1], [2, 1], [1, 1], [1, 0], [2, 0]],
             [[0, 3], [1, 2], [3, 1], [1, 3], [2, 1]]]
    results = [2, 1, 0]
    for test, result in zip(tests, results):
        assert Solution.min_area_free_rect(test) == result


def problem_5() -> None:
    """Problem 5."""
    tests = [(1, 0, 0, 1, -1, 3, 1), (1, 0, 0, -1, 0, 0, 1),
             (1, 1, 1, -3, -3, 3, 3)]
    results = [True, True, True]
    for test, result in zip(tests, results):
        assert Solution.check_overlap(*test) == result


def main():
    """My function."""
    problem_1()
    problem_2()
    problem_3()
    problem_4()
    problem_5()


if __name__ == "__main__":
    main()
