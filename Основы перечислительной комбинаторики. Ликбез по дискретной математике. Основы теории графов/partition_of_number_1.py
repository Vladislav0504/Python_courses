"""Partition of number."""
from sys import stdin, stdout


def main():
    """My function."""
    input()
    for line in stdin:
        p_0, p_1, p_2, p_3 = map(int, line.split())
        q_n = p_0 - p_1 - p_2 + p_3
        stdout.write(f"{q_n}\n")


if __name__ == "__main__":
    main()
