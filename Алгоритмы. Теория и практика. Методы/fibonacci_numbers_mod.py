"""Fibonacci numbers."""


def fibonacci_mod(num_n: int, num_m: int = 10) -> int:
    """Fibonacci number modulo num_m."""
    num_1, num_2 = 1, 0
    for i in range(num_n):
        num_1, num_2 = num_2, (num_1 + num_2) % num_m
        if num_1 == 1 and num_2 == 0:
            num_n %= i + 1
            break
    num_1, num_2 = 1, 0
    for _ in range(num_n):
        num_1, num_2 = num_2, (num_1 + num_2) % num_m
    return num_2


def main():
    """My function."""
    numbers = map(int, input().split())
    print(fibonacci_mod(*numbers))


if __name__ == "__main__":
    main()
