"""Sets."""


def main():
    """My function."""
    num_n, num_m, num_k, num_x = (int(input()) for _ in range(4))
    num_y, num_z, num_t, num_a = (int(input()) for _ in range(4))
    total_1, total_2 = num_n + num_m + num_k, num_x + num_y + num_z
    ans_3 = num_a - num_t - (total_2 - total_1)
    ans_2 = (total_1 << 1) - total_2 - 3 * num_t
    ans_1 = total_2 - total_1 - ans_2
    print(ans_1, ans_2, ans_3, sep="\n")


if __name__ == "__main__":
    main()
