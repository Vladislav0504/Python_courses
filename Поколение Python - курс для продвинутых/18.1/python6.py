"""Exam."""


def main():
    """My function."""
    with open("forbidden_words.txt", "r", encoding="utf8") as file_1:
        forbidden_words = set(file_1.read().split())
    file_name = input()
    with open(file_name, "r", encoding="utf8") as file_2:
        text = file_2.read()
        text_lower = text.lower()
        for word in forbidden_words:
            text_lower = text_lower.replace(word, "*" * len(word))
        text = list(text)
        for i, char in enumerate(text_lower):
            if char == "*":
                text[i] = "*"
        print("".join(text))


if __name__ == "__main__":
    main()
