"""Divide and conquer."""


def merge(arr_1: list[int], arr_2: list[int], k: int) -> (int, list[int]):
    """Merge."""
    array = []
    ind_1, ind_2 = 0, 0
    len_1, len_2 = len(arr_1), len(arr_2)
    while ind_1 < len_1 and ind_2 < len_2:
        if arr_1[ind_1] <= arr_2[ind_2]:
            array.append(arr_1[ind_1])
            ind_1 += 1
        else:
            array.append(arr_2[ind_2])
            k += len_1 - ind_1
            ind_2 += 1
    array.extend(arr_1[ind_1:])
    array.extend(arr_2[ind_2:])
    return k, array


def merge_sort(left: int, right: int, arr: list[int],
               k: int) -> (int, list[int]):
    """Mergesort."""
    if left < right:
        mid = left + right >> 1
        count_1, sort_1 = merge_sort(left, mid, arr, k)
        count_2, sort_2 = merge_sort(mid + 1, right, arr, k)
        return merge(sort_1, sort_2, count_1 + count_2)
    return k, [arr[left]]


def main():
    """My function."""
    num_n = int(input())
    array_a = list(map(int, input().split()))
    print(merge_sort(0, num_n - 1, array_a, 0)[0])


if __name__ == "__main__":
    main()
