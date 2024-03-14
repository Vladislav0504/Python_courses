"""Project."""
from random import choice


def get_word(word_list: list[str]) -> str:
    """Get word."""
    return choice(word_list).upper()


# функция получения текущего состояния
def display_hangman(tries: int) -> str:
    """Display hangman."""
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
                """,
                # голова, торс, обе руки, одна нога
                """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     /
                -
                """,
                # голова, торс, обе руки
                """
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |
                -
                """,
                # голова, торс и одна рука
                """
                --------
                |      |
                |      O
                |     \\|
                |      |
                |
                -
                """,
                # голова и торс
                """
                --------
                |      |
                |      O
                |      |
                |      |
                |
                -
                """,
                # голова
                """
                --------
                |      |
                |      O
                |
                |
                |
                -
                """,
                # начальное состояние
                """
                --------
                |      |
                |
                |
                |
                |
                -
                """]
    return stages[tries]


def get_letter(word: str) -> str:
    """Get letter or word."""
    while True:
        string = input("Назовите букву или слово: ").strip().upper()
        if string.isalpha() and (len(string) == 1 or len(string) == len(word)):
            return string
        print("Неправильный ввод!")


def play(word: str) -> None:
    """Play."""
    # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = "_" * len(word)
    word_completion_list = ["_"] * len(word)
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток
    print("Давайте играть в угадайку слов!")
    print(display_hangman(tries))
    print(word_completion)
    while not guessed and tries > 0:
        string = get_letter(word)
        if string in guessed_letters or string in guessed_words:
            print("Вы уже называли эту букву/это слово!")
            continue

        if len(string) == 1:
            guessed_letters.append(string)
            for i, char in enumerate(word):
                if char == string:
                    word_completion_list[i] = char
            word_completion = "".join(word_completion_list)
        else:
            guessed_words.append(string)
            if string == word:
                word_completion = word

        if string not in word:
            tries -= 1
        print(display_hangman(tries))
        print(word_completion)
        if word_completion == word:
            guessed = True
            print("Поздравляем, вы угадали слово! Вы победили!")
    if not guessed:
        print(f"Вы проиграли. Загаданное слово: {word}.")


def main():
    """My function."""
    word_list = ["КЛЮЧ", "КНИГА", "ЕНОТ", "МАШИНКА", "КОРОВА", "ТЕЛЕЖКА",
                 "ШЛЕМ", "КНОПКА", "ШНУР", "ЧЕРНЫЙ", "ВЛАСТЕЛИН", "СКАЙП",
                 "ДУБ", "ЧАСЫ", "ТРУБА", "ЕЛКА", "ИНСТИТУТ", "КОРОБКА",
                 "ТАБЛИЧКА", "ВОДА", "СКОВОРОДА", "МНОГОНОЖКА", "ЕВРЕЙ",
                 "ТЕРМИТ", "КАЧОК", "РУЛОН", "МАГНИТОФОН", "НОГА", "СЛОН",
                 "МИКРОВОЛНОВКА", "ТОРТ", "МАК", "ДЫМ", "ЧАЙКА", "ВАЛЕТ",
                 "ПЛИНТУС", "ШАПКА", "ДИНОЗАВР", "ТОРШЕР", "БАЛАЛАЙКА",
                 "БАНКА", "ЯХТА", "ОВЦА", "БАНАН", "АНИМЕ", "РАДУГА", "БУКВА",
                 "ВЕЛОСИПЕД", "БАНДЖО", "ГОЛУБЬ", "ВИНТОВКА", "КУБОК",
                 "ЖАСМИН", "ТЕЛЕФОН", "АНДРОИД", "ГОРА", "ХАЛАТ", "ЖЕТОН",
                 "ОБОД", "МЫЛО", "ЙОГ", "ШИШКА", "ДОЛЛАР", "КОЛОНКА", "КУБИК",
                 "ОМАР", "РАКЕТА", "МОРКОВКА", "ЗЕРКАЛО", "МОЛОТ", "ВОЗДУХ",
                 "ЗМЕЙ", "ЕЖ", "ПАЛЬМА", "МАСЛО", "ДИДЖЕЙ", "МЕШОК", "ТЮБИК",
                 "МОЗГ", "ПОЕЗД", "РОЗЕТКА", "ПАРАШЮТИСТ", "БЕЛКА", "ШПРОТЫ",
                 "САМОСВАЛ", "ПАЗЛ", "БУТЫЛКА", "КРЕМЛЬ", "ПИЦЦА", "МАКАРОНЫ",
                 "КОВЕР", "ЗУБЫ", "ЯРЛЫК", "КАШАЛОТ", "МАРС", "ШАКАЛ",
                 "ПОМАДА", "ДЖИП", "ЛЕЩ", "КАМЕНЬ", "ДИСК"]
    flag = True
    while flag:
        word = get_word(word_list)
        play(word)
        while True:
            answer = input("Хотите сыграть еще? (да или нет) ").strip().lower()
            if answer in ("да", "нет"):
                flag = answer == "да"
                break
            print("Ответ не ясен!")
    print("Спасибо, что играли в угадайку слов. Еще увидимся...")


if __name__ == "__main__":
    main()
