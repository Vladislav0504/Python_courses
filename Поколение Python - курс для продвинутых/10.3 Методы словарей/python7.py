"""Dictionaries."""
from sys import stdout


def main():
    """My function."""
    text, count = input(), {}
    for word in text.split():
        count[word] = count.get(word, -1) + 1
        stdout.write(f"{word}_{count[word]} " if count[word] else f"{word} ")


if __name__ == "__main__":
    main()
