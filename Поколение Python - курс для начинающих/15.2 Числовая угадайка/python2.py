"""Project."""
from random import randint


def is_valid(value: str, min_val: int, max_val: int) -> bool:
    """Is value valid?."""
    if max_val:
        return value.isdigit() and min_val <= int(value) <= max_val
    return value.isdigit() and min_val <= int(value)


def choose_max(min_num: int) -> int:
    """Choosing maximum natural number."""
    while True:
        max_num = input("Выберите максимальное натуральное"
                        " число для случайного выбора: ").strip()
        if is_valid(max_num, min_num, 0):
            return int(max_num)
        print("А может быть, все-таки введем натуральное число?")


def game() -> None:
    """Game."""
    min_num = 1
    max_num = choose_max(min_num)
    num, trying = randint(min_num, max_num), 0
    while True:
        number = input(f"Угадай число от {min_num} до {max_num}: ").strip()

        if not is_valid(number, min_num, max_num):
            print(f"А может быть, все-таки введем целое число"
                  f" от {min_num} до {max_num}?")
            continue

        number = int(number)
        trying += 1

        if number < num:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        elif number > num:
            print("Ваше число больше загаданного, попробуйте еще разок")
        else:
            print("Вы угадали, поздравляем!")
            print(f"Использовано попыток: {trying}.")
            break


def main():
    """My function."""
    print("Добро пожаловать в числовую угадайку!")
    flag = True
    while flag:
        game()
        while True:
            answer = input("Хотите сыграть еще? (да или нет) ").strip().lower()
            if answer in ("да", "нет"):
                flag = answer == "да"
                break
            print("Ответ не ясен!")
    print("Спасибо, что играли в числовую угадайку. Еще увидимся...")


if __name__ == "__main__":
    main()
