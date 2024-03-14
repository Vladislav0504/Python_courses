"""Random."""
from random import choice


def main():
    """My function."""
    length = int(input())
    start_1, end_1, start_2, end_2 = 65, 90, 97, 122
    codes = tuple(range(start_1, end_1 + 1)) + tuple(range(start_2, end_2 + 1))
    password = "".join(chr(choice(codes)) for _ in range(length))
    print(password)


if __name__ == "__main__":
    main()
