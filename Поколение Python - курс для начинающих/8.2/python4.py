"""Exam."""


def main():
    """My function."""
    num_n, num_m = int(input()), 19
    print("*" * num_m)
    print("".join(("*", " " * (num_m - 2), "*\n")) * (num_n - 2), end="")
    print("*" * num_m)


if __name__ == "__main__":
    main()
