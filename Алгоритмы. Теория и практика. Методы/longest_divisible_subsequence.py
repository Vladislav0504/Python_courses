"""Dynamic programming."""


def longest_divisible_sequence(num_n: int, array: list[int]) -> int:
    """Longest divisible subsequence."""
    tab = [1] * num_n
    for i in range(num_n):
        for j in range(i):
            if array[i] % array[j] == 0:
                tab[i] = max(tab[i], tab[j] + 1)
    return max(tab)


def main():
    """My function."""
    num_n = int(input())
    array = list(map(int, input().split()))
    print(longest_divisible_sequence(num_n, array))


if __name__ == "__main__":
    main()
