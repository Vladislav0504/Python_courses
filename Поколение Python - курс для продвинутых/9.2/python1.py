"""Exam."""


def main():
    """My function."""
    num_n, num_m, num_k, num_p = (int(input()) for _ in range(4))
    print(num_n - num_m - num_k + num_p)


if __name__ == "__main__":
    main()
