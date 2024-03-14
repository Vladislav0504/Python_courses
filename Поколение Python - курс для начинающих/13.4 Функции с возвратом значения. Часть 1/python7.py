"""Functions."""


def quick_merge(lst: list[list[int]]) -> list[int]:
    """General sorted list."""
    result = []
    for numbers in lst:
        result.extend(numbers)
    result.sort()
    return result


def main():
    """My function."""
    num_n = int(input())
    lst = [list(map(int, input().split())) for _ in range(num_n)]
    print(*quick_merge(lst))


if __name__ == "__main__":
    main()
