"""Int function."""


def main():
    """My function."""
    num = input()
    sum_num = sum(map(int, num))
    prod_num = 1
    for i in map(int, num):
        prod_num *= i
    print(f"Сумма цифр = {sum_num}")
    print(f"Произведение цифр = {prod_num}")


if __name__ == "__main__":
    main()
