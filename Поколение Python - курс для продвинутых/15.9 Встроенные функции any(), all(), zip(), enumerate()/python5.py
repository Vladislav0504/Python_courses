"""Functions."""


def main():
    """My function."""
    num_a, num_b = int(input()), int(input())
    print(*filter(lambda n: all(map(lambda x: n % (int(x) or n + 1) == 0,
                                    str(n))), range(num_a, num_b + 1)))


if __name__ == "__main__":
    main()
