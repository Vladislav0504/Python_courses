"""Dynamic programming."""


def longest_non_increasing_sequence(num_n: int, array: list[int]) -> list[int]:
    """Longest non-increasing subsequence."""
    indexes_of_maximum_ends, prev = [-1] * num_n, [-1] * num_n
    max_length = 0
    for j in range(num_n):
        left, right = 0, max_length
        while left <= right:
            mid = left + right >> 1
            if array[indexes_of_maximum_ends[mid]] >= array[j]:
                left = mid + 1
            else:
                right = mid - 1
        prev[j] = indexes_of_maximum_ends[left - 1]
        indexes_of_maximum_ends[left] = j
        if left == max_length:
            max_length += 1
    index = indexes_of_maximum_ends[max_length - 1]
    result = [0] * max_length
    for i in range(max_length - 1, -1, -1):
        result[i] = index + 1
        index = prev[index]
    return result


def main():
    """My function."""
    num_n = int(input())
    array = list(map(int, input().split()))
    sequence_indexes = longest_non_increasing_sequence(num_n, array + [-1])
    print(len(sequence_indexes))
    print(*sequence_indexes)


if __name__ == "__main__":
    main()
