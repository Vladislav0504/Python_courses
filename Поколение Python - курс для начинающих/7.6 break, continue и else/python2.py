"""Loops."""


def main():
    """My function."""
    num_n, k = int(input()), (5, 9, 17, 37, 78, 87)
    for i in range(1, num_n + 1):
        if i < k[0] or k[1] < i < k[2] or k[3] < i < k[4] or i > k[5]:
            print(i)


if __name__ == "__main__":
    main()
