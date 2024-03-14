"""Repetition."""


def main():
    """My function."""
    year, init = int(input()), 2000
    chinese_horoscope = ("Дракон", "Змея", "Лошадь", "Овца",
                         "Обезьяна", "Петух", "Собака", "Свинья",
                         "Крыса", "Бык", "Тигр", "Заяц")
    print(chinese_horoscope[(year - init) % len(chinese_horoscope)])


if __name__ == "__main__":
    main()
