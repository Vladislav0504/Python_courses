"""Greedy algorithms."""
from sys import stdin


def main():
    """My function."""
    input()
    intervals = [tuple(map(int, line.split())) for line in stdin]
    intervals.sort(reverse=True)
    points = [intervals[0][0]]
    for left, right in intervals[1:]:
        if right < points[-1]:
            points.append(left)
    print(len(points))
    print(*points)


if __name__ == "__main__":
    main()
