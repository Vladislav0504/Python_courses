"""Lists."""


def main():
    """My function."""
    keywords = ["False", "True", "None", "and", "with", "as", "assert",
                "break", "class", "continue", "def", "del", "elif", "else",
                "except", "finally", "try", "for", "from", "global", "if",
                "import", "in", "is", "lambda", "nonlocal", "not", "or",
                "pass", "raise", "return", "while", "yield"]
    new_keywords = [elem[1:] for elem in keywords]
    print(new_keywords)


if __name__ == "__main__":
    main()
