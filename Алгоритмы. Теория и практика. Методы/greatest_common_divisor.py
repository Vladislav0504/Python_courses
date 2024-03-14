"""Greatest common divisor."""


def greatest_common_divisor(num_a: int, num_b: int) -> int:
    """Greatest common divisor."""
    while num_a:
        num_b, num_a = num_a, num_b % num_a
    return num_b


def main():
    """My function."""
    num_a, num_b = map(int, input().split())
    print(greatest_common_divisor(num_a, num_b))


if __name__ == "__main__":
    main()
