"""Permutations."""


def permutations(numbers: list[int], num_k: int) -> list[list[int]]:
    """Permutations."""
    if num_k == 0:
        return [[]]
    result = []
    for i, num in enumerate(numbers):
        lst = permutations(numbers[:i] + numbers[i + 1:], num_k - 1)
        result.extend([[num] + lst_i for lst_i in lst])
    return result


def main():
    """My function."""
    num_n, k = map(int, input().split())
    numbers = list(range(num_n))
    print(*(" ".join(map(str, p)) for p in permutations(numbers, k)), sep="\n")


if __name__ == "__main__":
    main()
