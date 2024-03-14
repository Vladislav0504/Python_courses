"""Project."""
from random import choices


def answer_count(question: str) -> int:
    """Get integer answer."""
    while True:
        number = input(f"{question} ").strip()
        if number.isdigit():
            return int(number)
        print("А может быть, все-таки введем целое неотрицательное число?")


def answer_yes_no(question: str) -> bool:
    """Get boolean answer."""
    while True:
        answer = input(f"{question} (да или нет) ").strip().lower()
        if answer in ("да", "нет"):
            return answer == "да"
        print("Ответ не ясен!")


def answers(char_lst: list[str]) -> (int, int, str):
    """Get general answer."""
    digits, up_letters, low_letters, punctuation, ambiguous_chars = char_lst
    question_count = ["Какое будет количество паролей для генерации?",
                      "Какая будет длина одного пароля?"]
    question_yes_no = [f"Включать ли цифры {digits}?",
                       f"Включать ли прописные буквы {up_letters}?",
                       f"Включать ли строчные буквы {low_letters}?",
                       f"Включать ли символы {punctuation}?",
                       f"Исключать ли неоднозначные символы {ambiguous_chars}?"
                       ]
    chars = ""
    for i, question in enumerate(question_yes_no):
        answer = answer_yes_no(question)
        if i == len(question_yes_no) - 1 and answer:
            for char in char_lst[i]:
                chars = chars.replace(char, "")
        elif answer:
            chars += char_lst[i]
    passwords_number = answer_count(question_count[0])
    passwords_length = answer_count(question_count[1])
    return passwords_number, passwords_length, chars


def generate_password(length: int, chars: str) -> str:
    """Generate password."""
    return "".join(choices(chars, k=length if chars else 0))


def main():
    """My function."""
    digits = "0123456789"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuation = "!#$%&*+-=?@^_"
    ambiguous_chars = "il1Lo0O"
    char_lst = [digits, uppercase_letters, lowercase_letters,
                punctuation, ambiguous_chars]
    passwords_number, passwords_length, chars = answers(char_lst)
    print("Пароли:")
    for _ in range(passwords_number):
        print(generate_password(passwords_length, chars))


if __name__ == "__main__":
    main()
