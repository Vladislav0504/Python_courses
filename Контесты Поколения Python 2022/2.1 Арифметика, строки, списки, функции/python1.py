"""Contest."""


def main():
    """My function."""
    d_1, d_2, d_3 = (int(input()) for _ in range(3))
    dist = min(d_1 + d_2 + d_3, d_1 + d_2 << 1, d_1 + d_3 << 1, d_2 + d_3 << 1)
    print(dist)


if __name__ == "__main__":
    main()
