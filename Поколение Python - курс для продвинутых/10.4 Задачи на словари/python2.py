"""Dictionaries."""


def main():
    """My function."""
    word_1, word_2, count = input(), input(), {}
    for char_1 in word_1:
        count[char_1] = count.get(char_1, 0) + 1
    for char_2 in word_2:
        count[char_2] = count.get(char_2, 0) - 1
    print("NO" if any(count.values()) else "YES")


if __name__ == "__main__":
    main()
