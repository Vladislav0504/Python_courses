"""Sets."""


def main():
    """My function."""
    marks = tuple(set(map(int, input().split())) for _ in range(3))
    result = sorted(set.union(*marks) - set.intersection(*marks))
    print(*result)


if __name__ == "__main__":
    main()
