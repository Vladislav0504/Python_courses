"""Functions."""


def is_one_away(word_1: str, word_2: str) -> bool:
    """Is one away?."""
    if len(word_1) != len(word_2):
        return False
    return sum(char_1 != char_2 for char_1, char_2 in zip(word_1, word_2)) == 1


def main():
    """My function."""
    txt_1, txt_2 = input(), input()
    print(is_one_away(txt_1, txt_2))


if __name__ == "__main__":
    main()
