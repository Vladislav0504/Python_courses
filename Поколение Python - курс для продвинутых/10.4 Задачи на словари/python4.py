"""Dictionaries."""
from sys import stdin


def main():
    """My function."""
    num_n, dictionary = int(input()), {}
    for _ in range(num_n):
        word_1, word_2 = stdin.readline().strip().split()
        dictionary[word_1] = word_2
        dictionary[word_2] = word_1
    print(dictionary[input()])


if __name__ == "__main__":
    main()
