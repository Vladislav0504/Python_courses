"""Strings."""


def main():
    """My function."""
    string = input().lower()
    pair = (("Аденин", "а"), ("Гуанин", "г"), ("Цитозин", "ц"), ("Тимин", "т"))
    print(*(": ".join((x, str(string.count(y)))) for x, y in pair), sep="\n")


if __name__ == "__main__":
    main()
