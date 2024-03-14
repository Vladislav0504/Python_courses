"""Conditions."""


def main():
    """My function."""
    num_1, num_2, num_3 = (int(input()) for _ in range(3))
    print("YES" if num_2 - num_1 == num_3 - num_2 else "NO")


if __name__ == "__main__":
    main()
