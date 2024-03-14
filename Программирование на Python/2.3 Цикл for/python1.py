"""Loops."""


def main():
    """My function."""
    num_a, num_b = int(input()), int(input())
    num_c, num_d = int(input()), int(input())
    print(" ", *range(num_c, num_d + 1), sep="\t")
    left = num_a * num_c
    right = left + num_a * (num_d - num_c) + 1
    for i in range(num_a, num_b + 1):
        print(i, *range(left, right, i), sep="\t")
        left += num_c
        right += num_d


if __name__ == "__main__":
    main()
