"""Sets."""


def main():
    """My function."""
    marks = set().union(*(map(int, input().split()) for _ in range(3)))
    max_mark = 10
    result = sorted(set(range(max_mark + 1)) - marks)
    print(*result)


if __name__ == "__main__":
    main()
