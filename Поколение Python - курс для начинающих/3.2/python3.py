"""Exam."""


def main():
    """My function."""
    num_a, num_b, num_c, num_d = (int(input()) for _ in range(4))
    result = num_a**num_b + num_c**num_d
    print(result)


if __name__ == "__main__":
    main()
