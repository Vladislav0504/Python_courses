"""Conditions."""


def main():
    """My function."""
    n_1, n_2, n_3 = (int(input()) for _ in range(3))
    if n_1 + n_2 > n_3 and n_1 + n_3 > n_2 and n_2 + n_3 > n_1:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
