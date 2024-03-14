"""Loops."""


def main():
    """My function."""
    num_n = int(input())
    for i in range(num_n + 1):
        square = i**2
        print(f"Квадрат числа {i} равен {square}")


if __name__ == "__main__":
    main()
