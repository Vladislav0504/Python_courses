"""Exam."""


def main():
    """My function."""
    set_1, set_2 = (set(input().split()) for _ in range(2))
    union = set_1 | set_2
    print(*sorted(union))


if __name__ == "__main__":
    main()
