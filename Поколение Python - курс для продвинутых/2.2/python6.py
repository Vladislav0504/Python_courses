"""Repetition."""
from sys import stdin


def solution(nums: dict[int, bool], prod: int) -> str:
    """Solution."""
    for i, value in nums.items():
        con_1 = i**2 == prod and (value or i == 0 and len(nums) > 1)
        con_2 = i**2 != prod and i and prod % i == 0 and prod // i in nums
        if con_1 or con_2:
            return "ДА"
    return "НЕТ"


def main():
    """My function."""
    num_n, nums = int(input()), {}
    for _ in range(num_n):
        num = int(stdin.readline())
        nums[num] = num in nums
    number = int(input())
    print(solution(nums, number))


if __name__ == "__main__":
    main()
