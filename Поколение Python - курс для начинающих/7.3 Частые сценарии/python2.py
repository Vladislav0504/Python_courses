"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    print(sum(int(input()) for _ in range(num_n)))


if __name__ == "__main__":
    main()
