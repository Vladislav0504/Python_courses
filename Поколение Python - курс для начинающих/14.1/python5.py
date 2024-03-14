"""Exam."""


def get_month(language: str, number: int) -> str:
    """Month on language."""
    months = (("january", "february", "march", "april", "may", "june", "july",
               "august", "september", "october", "november", "december"),
              ("январь", "февраль", "март", "апрель", "май", "июнь", "июль",
               "август", "сентябрь", "октябрь", "ноябрь", "декабрь"))
    return months[language == "ru"][number - 1]


def main():
    """My function."""
    language, num = input(), int(input())
    print(get_month(language, num))


if __name__ == "__main__":
    main()
