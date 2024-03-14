"""Tuples."""
from sys import stdout


def main():
    """My function."""
    num_n, num_1, num_2, num_3 = int(input()), 1, 1, 1
    stdout.write("1 " * min(num_n, 3))
    for _ in range(num_n - 3):
        num_1, num_2, num_3 = num_2, num_3, num_1 + num_2 + num_3
        stdout.write(f"{num_3} ")


if __name__ == "__main__":
    main()
