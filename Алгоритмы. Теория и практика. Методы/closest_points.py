"""Divide and conquer.

Good program.
"""
from sys import stdin

from itertools import combinations


def dist_2(p_1: (int, int), p_2: (int, int)) -> int:
    """Squared distance."""
    return (p_1[0] - p_2[0])**2 + (p_1[1] - p_2[1])**2


def merge(points_1: list[(int, int)],
          points_2: list[(int, int)]) -> list[(int, int)]:
    """Merge by the second coordinate."""
    points = []
    index_1, index_2, len_1, len_2 = 0, 0, len(points_1), len(points_2)
    while index_1 < len_1 and index_2 < len_2:
        if points_1[index_1][1] <= points_2[index_2][1]:
            points.append(points_1[index_1])
            index_1 += 1
        else:
            points.append(points_2[index_2])
            index_2 += 1
    points.extend(points_1[index_1:])
    points.extend(points_2[index_2:])
    return points


def min_dist(points: list[(int, int)]) -> (int, list[(int, int)]):
    """Minimum distance."""
    if len(points) <= 3:
        degree = 32
        dist = 1 << degree
        for point_1, point_2 in combinations(points, 2):
            dist = min(dist, dist_2(point_1, point_2))
        return dist, sorted(points, key=lambda point: point[1])
    mid = len(points) >> 1
    x_mid = points[mid][0]
    distance, points_1 = min_dist(points[:mid])
    distance_2, points_2 = min_dist(points[mid:])
    distance = min(distance, distance_2)
    points = merge(points_1, points_2)
    strip = [point for point in points if (point[0] - x_mid)**2 < distance]
    for i, p_1 in enumerate(strip):
        for p_2 in strip[i + 1:i + 8]:
            distance = min(distance, dist_2(p_1, p_2))
    return distance, points


def main():
    """My function."""
    input()
    points = [tuple(map(int, point.split())) for point in stdin]
    points.sort()
    print(min_dist(points)[0]**0.5)


if __name__ == "__main__":
    main()
