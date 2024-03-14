"""Sets."""


def main():
    """My function."""
    num_1, num_2 = (set(map(int, input())) for _ in range(2))
    print("YES" if num_1 & num_2 else "NO")


if __name__ == "__main__":
    main()
