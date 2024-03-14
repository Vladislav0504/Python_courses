"""Exam."""


def main():
    """My function."""
    num_a, num_b = int(input()), int(input())
    result_1 = (num_a + num_b)**2
    result_2 = num_a**2 + num_b**2
    print(f"Квадрат суммы {num_a} и {num_b} равен {result_1}")
    print(f"Сумма квадратов {num_a} и {num_b} равна {result_2}")


if __name__ == "__main__":
    main()
