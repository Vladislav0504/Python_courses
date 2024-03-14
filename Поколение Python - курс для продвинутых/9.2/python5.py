"""Exam."""


def main():
    """My function."""
    first, second = (set(map(int, input().split())) for _ in range(2))
    result = first & second
    print(*sorted(result, reverse=True) if result else ("BAD DAY",))


if __name__ == "__main__":
    main()
