"""Project."""


def answer_int(question: str) -> int:
    """Get integer answer."""
    while True:
        answer = input(f"{question} ").strip()
        if answer.isdigit():
            return int(answer)
        print("А может быть, все-таки введем целое неотрицательное число?")


def answer_string(question: str, answers: list[str]) -> str:
    """Get string answer."""
    answers_text = "/".join(answers)
    while True:
        answer = input(f"{question} ({answers_text}) ").strip().lower()
        if answer in answers:
            return answer
        print("Ответ не ясен!")


def caesar(text: str, direction: str, language: str, rotate: int) -> str:
    """Caesar's cipher."""
    lengths, result = {"русский": 32, "английский": 26}, []
    mod, is_encrypt = lengths[language], direction == "шифрование"
    init_ords = {("русский", True): ord("А"),
                 ("русский", False): ord("а"),
                 ("английский", True): ord("A"),
                 ("английский", False): ord("a")}
    rotate %= mod
    for char in text:
        if char.isalpha():
            init_ord = init_ords[language, char.isupper()]
            order = ord(char) - init_ord + (-1)**(is_encrypt + 1) * rotate
            char = chr(order % mod + init_ord)
        result.append(char)
    return "".join(result)


def main():
    """My function."""
    directions = ["шифрование", "дешифрование"]
    languages = ["русский", "английский"]
    questions = ["Какое направление?", "Какой язык алфавита?",
                 "Какой шаг сдвига?"]
    direction = answer_string(questions[0], directions)
    language = answer_string(questions[1], languages)
    rotate = answer_int(questions[2])
    text = input("Введите строку обрабатываемого текста: ")
    print(caesar(text, direction, language, rotate))


if __name__ == "__main__":
    main()
