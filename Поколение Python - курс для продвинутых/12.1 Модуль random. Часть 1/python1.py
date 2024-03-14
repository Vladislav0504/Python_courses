"""Random."""
from random import choice


def main():
    """My function."""
    num_n, variants = int(input()), ("Орел", "Решка")
    print(*(choice(variants) for _ in range(num_n)), sep="\n")


if __name__ == "__main__":
    main()
