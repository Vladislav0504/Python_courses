"""Random."""
from random import shuffle


def main():
    """My function."""
    word = input()
    lst = list(word)
    shuffle(lst)
    anagram = "".join(lst)
    print(anagram)


if __name__ == "__main__":
    main()
