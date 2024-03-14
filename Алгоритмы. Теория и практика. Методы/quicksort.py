"""Divide and conquer.

Good program.
"""
from random import randint

from sys import stdout, stdin


def partition(left: int, right: int, array: list[int]) -> (int, int):
    """Partition."""
    num = array[left]
    i, j = left, left
    for k in range(left + 1, right + 1):
        elem = array[k]
        if elem < num:
            j += 1
            array[i], array[k], array[j] = elem, array[j], num
            i += 1
        elif elem == num:
            j += 1
            array[k], array[j] = array[j], num
    return i, j


def quick_sort(left: int, right: int, array: list[int]) -> None:
    """Quick sort."""
    if left < right:
        rand = randint(left, right)
        array[left], array[rand] = array[rand], array[left]
        i, j = partition(left, right, array)
        quick_sort(left, i - 1, array)
        quick_sort(j + 1, right, array)


def main():
    """My function."""
    num_n, _ = map(int, input().split())
    array_a, array_b = [0] * num_n, [0] * num_n
    for i in range(num_n):
        array_a[i], array_b[i] = map(int, stdin.readline().split())
    quick_sort(0, num_n - 1, array_a)
    quick_sort(0, num_n - 1, array_b)
    for point in map(int, input().split()):
        left, right = 0, num_n - 1
        while left <= right:
            mid = left + right >> 1
            if array_a[mid] <= point:
                left = mid + 1
            else:
                right = mid - 1
        count = left
        left, right = 0, num_n - 1
        while left <= right:
            mid = left + right >> 1
            if array_b[mid] >= point:
                right = mid - 1
            else:
                left = mid + 1
        count -= left
        stdout.write(f"{count} ")


if __name__ == "__main__":
    main()
