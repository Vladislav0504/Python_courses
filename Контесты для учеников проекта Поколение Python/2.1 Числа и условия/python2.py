"""Contest."""


def main():
    """My function."""
    numbers = tuple(int(input()) for _ in range(3))
    print("YES" if sum(i & 1 for i in numbers) in (1, 2) else "NO")


if __name__ == "__main__":
    main()
