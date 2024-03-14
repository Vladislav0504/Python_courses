"""Regular expressions."""
from sys import stdin

from re import fullmatch


def main():
    """My function."""
    pattern = r"(0|(1(01*0)*1))+\s*"  # конечный автомат (0)<--1-->()<--0-->(1)
    # переходы (n % 3 == 0)<---->(n % 3 == 1)<---->(n % 3 == 2)
    print(*(line for line in stdin if fullmatch(pattern, line)), sep="")


if __name__ == "__main__":
    main()
