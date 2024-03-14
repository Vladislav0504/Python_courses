"""Loops."""


def main():
    """My function."""
    num_a, num_b = int(input()), int(input())
    if num_a >= 0:
        print((num_b + 1) // 5 - num_a // 5)
    elif num_b <= 0:
        print((-num_a + 1) // 5 - (-num_b) // 5)
    else:
        print((num_b + 1) // 5 + (-num_a + 1) // 5)


if __name__ == "__main__":
    main()
