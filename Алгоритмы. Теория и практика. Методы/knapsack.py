"""Dynamic programming."""


def knapsack(num_w: int, array_w: list[int]) -> int:
    """Knapsack."""
    prev, cur = [0] * (num_w + 1), [0] * (num_w + 1)
    for elem_w in array_w:
        prev, cur = cur, prev
        for weight_0 in range(1, min(elem_w, num_w + 1)):
            cur[weight_0] = prev[weight_0]
        for weight in range(elem_w, num_w + 1):
            cur[weight] = max(prev[weight], prev[weight - elem_w] + elem_w)
    return cur[num_w]


def main():
    """My function."""
    num_w, _ = map(int, input().split())
    array_w = list(map(int, input().split()))
    print(knapsack(num_w, array_w))


if __name__ == "__main__":
    main()
