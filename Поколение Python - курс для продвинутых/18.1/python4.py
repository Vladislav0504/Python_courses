"""Exam."""


def main():
    """My function."""
    with open("words.txt", "r", encoding="utf8") as inp:
        my_words = inp.read().split()
        maximum = max(map(len, my_words))
        print(*filter(lambda w: len(w) == maximum, my_words), sep="\n")


if __name__ == "__main__":
    main()
