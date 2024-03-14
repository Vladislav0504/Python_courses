"""Functions."""


def merge(list_1: list[int], list_2: list[int]) -> list[int]:
    """General sorted list."""
    result = []
    p_1, p_2, len_1, len_2 = 0, 0, len(list_1), len(list_2)
    while p_1 < len_1 and p_2 < len_2:
        if list_1[p_1] < list_2[p_2]:
            result.append(list_1[p_1])
            p_1 += 1
        else:
            result.append(list_2[p_2])
            p_2 += 1
    result.extend(list_1[p_1:])
    result.extend(list_2[p_2:])
    return result


def main():
    """My function."""
    numbers_1 = list(map(int, input().split()))
    numbers_2 = list(map(int, input().split()))
    print(merge(numbers_1, numbers_2))


if __name__ == "__main__":
    main()
