"""Loops."""


def main():
    """My function."""
    num_n, total = int(input()), 0
    for i in range(1, int(num_n**0.5) + 1):
        if i**2 == num_n:
            total += i
        elif num_n % i == 0:
            total += i + num_n // i
    print(total)


if __name__ == "__main__":
    main()
