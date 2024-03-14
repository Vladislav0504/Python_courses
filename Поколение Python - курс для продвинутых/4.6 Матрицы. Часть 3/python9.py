"""Matrices."""


def main():
    """My function."""
    num_n, num_m = map(int, input().split())
    matrix, count = tuple([0] * num_m for _ in range(num_n)), 1
    for k in range(num_m + num_n - 1):
        for i in range(max(0, k - num_m + 1), min(k, num_n - 1) + 1):
            matrix[i][k - i] = count
            count += 1
    for row in matrix:
        print(*(x + " " * (3 - len(x)) for x in map(str, row)), sep="")


if __name__ == "__main__":
    main()
