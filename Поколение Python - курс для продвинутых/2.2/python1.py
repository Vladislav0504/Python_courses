"""Repetition."""
from sys import stdin


def quarter(coord_x: int, coord_y: int) -> int:
    """Quarter."""
    if coord_x > 0 and coord_y > 0:
        return 1
    if coord_x < 0 < coord_y:
        return 2
    if coord_x < 0 and coord_y < 0:
        return 3
    if coord_y < 0 < coord_x:
        return 4
    return 0


def main():
    """My function."""
    reader = (map(int, line.split()) for line in stdin)
    quarters = ("Первая четверть:", "Вторая четверть:",
                "Третья четверть:", "Четвертая четверть:")
    counts, _ = [0, 0, 0, 0, 0], next(reader)
    for coord_x, coord_y in reader:
        counts[quarter(coord_x, coord_y)] += 1
    print(*(f"{q} {c}" for q, c in zip(quarters, counts[1:])), sep="\n")


if __name__ == "__main__":
    main()
