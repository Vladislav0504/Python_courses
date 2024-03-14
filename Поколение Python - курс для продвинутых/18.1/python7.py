"""Exam."""


def main():
    """My function."""
    my_dict = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e",
               "ё": "jo", "ж": "zh", "з": "z", "и": "i", "й": "j", "к": "k",
               "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
               "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "c",
               "ч": "ch", "ш": "sh", "щ": "shh", "ъ": "*", "ы": "y", "ь": "'",
               "э": "je", "ю": "ju", "я": "ya"}
    with open("cyrillic.txt", "r", encoding="utf8") as inp:
        with open("transliteration.txt", "w", encoding="utf8") as out:
            text = list(inp.read())
            for i, char in enumerate(text):
                text[i] = my_dict.get(char, char)
                if char.isupper():
                    text[i] = my_dict.get(char.lower(), char).title()
            out.write("".join(text))


if __name__ == "__main__":
    main()
