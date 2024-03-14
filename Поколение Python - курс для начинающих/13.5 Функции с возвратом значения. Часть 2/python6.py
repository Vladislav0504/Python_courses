"""Functions."""


def is_palindrome(text: str) -> bool:
    """Is text palindrome?."""
    text = text.lower()
    for char in " ,.!?-":
        text = text.replace(char, "")
    return text == text[::-1]


def main():
    """My function."""
    txt = input()
    print(is_palindrome(txt))


if __name__ == "__main__":
    main()
