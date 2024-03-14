"""Matrices."""
from sys import stdin


def main():
    """My function."""
    num_n = int(input())
    matrix = tuple(tuple(map(int, line.split())) for line in stdin)
    upper, right, lower, left = 0, 0, 0, 0
    for i, row in enumerate(matrix):
        upper += sum(row[i + 1:num_n - i - 1])
        left += sum(row[:min(i, num_n - i - 1)])
        right += sum(row[max(i + 1, num_n - i):])
        lower += sum(row[num_n - i:i])
    print("Верхняя четверть:", upper)
    print("Правая четверть:", right)
    print("Нижняя четверть:", lower)
    print("Левая четверть:", left)


if __name__ == "__main__":
    main()
