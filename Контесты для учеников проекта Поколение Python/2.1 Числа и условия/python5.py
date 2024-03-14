"""Contest."""


def main():
    """My function."""
    n_0, m_0, k = int(input()), int(input()), int(input())
    print("YES" if k <= n_0 * m_0 and 0 in (k % n_0, k % m_0) else "NO")


if __name__ == "__main__":
    main()
