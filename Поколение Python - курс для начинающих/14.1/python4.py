"""Exam."""


def number_to_words(num: int) -> str:
    """Translate number to russian words."""
    nums_1 = ("", "один", "два", "три", "четыре", "пять", "шесть", "семь",
              "восемь", "девять", "десять", "одиннадцать", "двенадцать",
              "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
              "семнадцать", "восемнадцать", "девятнадцать")
    nums_2 = ("", "десять", "двадцать", "тридцать", "сорок", "пятьдесят",
              "шестьдесят", "семьдесят", "восемьдесят", "девяносто")
    if num < len(nums_1):
        return nums_1[num]
    return " ".join((nums_2[num // 10], nums_1[num % 10]))


def main():
    """My function."""
    num = int(input())
    print(number_to_words(num))


if __name__ == "__main__":
    main()
