"""Dynamic programming."""


def stairs(array: list[int]) -> int:
    """Stairs."""
    sum_0, sum_1 = 0, 0
    for step in array:
        sum_0, sum_1 = sum_1, max(sum_1, sum_0) + step
    return sum_1


def main():
    """My function."""
    input()
    array = list(map(int, input().split()))
    print(stairs(array))


if __name__ == "__main__":
    main()
