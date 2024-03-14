"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    fib_0, fib_1 = 1, 0
    for _ in range(num_n):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        print(fib_1, end=" ")


if __name__ == "__main__":
    main()
