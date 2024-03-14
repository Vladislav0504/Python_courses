"""Greedy algorithms."""
from sys import stdin


def main():
    """My function."""
    _, num_w = map(int, input().split())
    costs_weights, res = [tuple(map(int, line.split())) for line in stdin], 0
    costs_weights.sort(reverse=True, key=lambda c_w: (c_w[0] / c_w[1], c_w[1]))
    for cost, weight in costs_weights:
        if num_w < weight:
            res += cost / weight * num_w
            break
        res += cost
        num_w -= weight
    print(res)


if __name__ == "__main__":
    main()
