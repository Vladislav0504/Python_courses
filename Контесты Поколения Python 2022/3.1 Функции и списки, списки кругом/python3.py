"""Contest."""


def main():
    """My function."""
    word, vowels, num_n = input(), "аеёиоуыэюя", int(input())
    indexes = [i for i, char in enumerate(word) if char in vowels]
    for _ in range(num_n):
        new_word = input()
        if indexes == [i for i, char in enumerate(new_word) if char in vowels]:
            print(new_word)


if __name__ == "__main__":
    main()
