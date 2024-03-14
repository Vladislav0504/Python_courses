"""Loops."""


def main():
    """My function."""
    num_a, num_b = int(input()), int(input())
    max_num, max_total = 0, 0
    for i in range(num_b, num_a - 1, -1):
        total = 0
        for j in range(1, int(i**0.5) + 1):
            if j**2 == i:
                total += j
            elif i % j == 0:
                total += j + i // j
        if total > max_total:
            max_num, max_total = i, total
    print(max_num, max_total)


if __name__ == "__main__":
    main()
