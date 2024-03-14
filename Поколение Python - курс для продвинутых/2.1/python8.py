"""Repetition."""


def main():
    """My function."""
    num_n, num_k = int(input()), int(input())
    result = 0
    for i in range(1, num_n + 1):
        result = (result + num_k) % i
    print(1 + result)


if __name__ == "__main__":
    main()
