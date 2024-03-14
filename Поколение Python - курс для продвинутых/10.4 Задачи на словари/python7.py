"""Dictionaries."""
from sys import stdin


def main():
    """My function."""
    encrypted, _ = input(), input()
    frequencies, dictionary = {}, {}
    for char in encrypted:
        frequencies[char] = frequencies.get(char, 0) + 1
    for line in stdin:
        letter, frequency = line.split(": ")
        dictionary[int(frequency)] = letter
    print(*(dictionary[frequencies[key]] for key in encrypted), sep="")


if __name__ == "__main__":
    main()
