"""Sets."""


def main():
    """My function."""
    marks = tuple(set(map(int, input().split())) for _ in range(3))
    result = sorted(marks[0] & marks[1] - marks[2], reverse=True)
    print(*result)


if __name__ == "__main__":
    main()
