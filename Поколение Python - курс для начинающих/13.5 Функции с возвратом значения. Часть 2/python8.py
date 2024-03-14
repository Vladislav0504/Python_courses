"""Functions."""


def is_correct_bracket(text: str) -> bool:
    """Is bracket sequence correct?."""
    open_brackets = 0
    for char in text:
        if char == "(":
            open_brackets += 1
        else:
            open_brackets -= 1
            if open_brackets < 0:
                return False
    return open_brackets == 0


def main():
    """My function."""
    txt = input()
    print(is_correct_bracket(txt))


if __name__ == "__main__":
    main()
