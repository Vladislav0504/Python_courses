"""Problems."""


def main():
    """My function."""
    alphabet, encrypt, encode, decode = input(), input(), input(), input()
    dict_1 = dict(zip(alphabet, encrypt))
    dict_2 = dict(zip(encrypt, alphabet))
    print(*(dict_1[char_1] for char_1 in encode), sep="")
    print(*(dict_2[char_2] for char_2 in decode), sep="")


if __name__ == "__main__":
    main()
