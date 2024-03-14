"""Exam."""


def main():
    """My function."""
    num_n = int(input())
    matrix = tuple(tuple(abs(i - j) for j in range(num_n))
                   for i in range(num_n))
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
