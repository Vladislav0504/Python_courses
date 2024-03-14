"""Types."""


def main():
    """My function."""
    l_1, l_2, l_3 = sorted(map(len, (input() for _ in range(3))))
    print("YES" if l_2 << 1 == l_1 + l_3 else "NO")


if __name__ == "__main__":
    main()
