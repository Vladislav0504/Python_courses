"""Exam."""


def main():
    """My function."""
    first, second = (set(map(int, input().split())) for _ in range(2))
    print("YES" if first == second else "NO")


if __name__ == "__main__":
    main()
