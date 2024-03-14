"""Functions."""


def number_of_factors(num: int) -> int:
    """Count of divisors."""
    count = sum(num % i == 0 for i in range(1, int(num**0.5) + 1)) << 1
    count -= int(num**0.5)**2 == num
    return count


def main():
    """My function."""
    num = int(input())
    print(number_of_factors(num))


if __name__ == "__main__":
    main()
