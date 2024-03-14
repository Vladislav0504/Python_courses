"""Sets."""


def main():
    """My function."""
    num_n, num_m, num_k = (int(input()) for _ in range(3))
    num_x, num_y, num_z = (int(input()) for _ in range(3))
    total = num_z + num_n + num_m + num_k - num_x - num_y
    print(total)


if __name__ == "__main__":
    main()
