"""Random."""
from random import sample


def main():
    """My function."""
    size, min_num, max_num = 5, 1, 75
    numbers = sample(range(min_num, max_num + 1), size**2)
    table = [numbers[i:i + size] for i in range(0, size**2, size)]
    table[size >> 1][size >> 1] = 0
    for row in table:
        print(*row)


if __name__ == "__main__":
    main()
