"""Functions."""


def get_factors(num: int) -> list[int]:
    """Factors of number."""
    lst = [i for i in range(1, int(num**0.5) + 1) if num % i == 0]
    start = -1 - (lst[-1]**2 == num)
    lst.extend([num // k for k in lst[start::-1]])
    return lst


def main():
    """My function."""
    num = int(input())
    print(get_factors(num))


if __name__ == "__main__":
    main()
