"""Repetition."""


def main():
    """My function."""
    str_1, str_2 = input(), input()
    variants = ("камень", "ящерица", "Спок", "ножницы", "бумага")
    result = ("ничья", "Руслан", "Тимур", "Руслан", "Тимур")
    print(result[variants.index(str_1) - variants.index(str_2)])


if __name__ == "__main__":
    main()
