"""Divide and conquer."""
from sys import stdout


def main():
    """My function."""
    num_n, *array_a = map(int, input().split())
    _, *array_b = map(int, input().split())
    for b_i in array_b:
        index = -1
        left, right = 0, num_n - 1
        while left <= right:
            mid = left + right >> 1
            if array_a[mid] == b_i:
                index = mid + 1
                break
            if array_a[mid] > b_i:
                right = mid - 1
            else:
                left = mid + 1
        stdout.write(f"{index} ")


if __name__ == "__main__":
    main()
