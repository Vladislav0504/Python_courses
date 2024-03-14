"""Dictionaries."""
from sys import stdin


def main():
    """My function."""
    reader, words = (line.strip() for line in stdin), {}
    num_n = int(next(reader))
    for _ in range(num_n):
        key, value = next(reader).split(": ")
        words[key.lower()] = value
    next(reader)
    print(*(words.get(w.lower(), "Не найдено") for w in reader), sep="\n")


if __name__ == "__main__":
    main()
