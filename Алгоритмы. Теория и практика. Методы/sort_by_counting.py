"""Divide and conquer."""


def count_sort(array: list[int], num_n: int, max_value: int) -> list[int]:
    """Sort by counting."""
    count = [0] * (max_value + 1)
    for i in array:
        count[i] += 1
    for k in range(1, max_value + 1):
        count[k] += count[k - 1]
    result = [0] * num_n
    for j in array:
        count[j] -= 1
        result[count[j]] = j
    return result


def main():
    """My function."""
    num_n = int(input())
    array = list(map(int, input().split()))
    print(*count_sort(array, num_n, 10))


if __name__ == "__main__":
    main()
