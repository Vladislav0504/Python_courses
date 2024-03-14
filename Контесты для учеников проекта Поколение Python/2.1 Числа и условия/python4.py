"""Contest."""


def main():
    """My function."""
    num_a, num_b = int(input()), int(input())
    num_c, num_d = int(input()), int(input())
    print(num_a + max(num_d - num_b, 0) * num_c)


if __name__ == "__main__":
    main()
