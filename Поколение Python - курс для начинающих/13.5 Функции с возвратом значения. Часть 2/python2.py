"""Functions."""


def is_prime(num: int) -> bool:
    """Is number prime?."""
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    """My function."""
    num = int(input())
    print(is_prime(num))


if __name__ == "__main__":
    main()
