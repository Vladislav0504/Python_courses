"""Dictionaries."""


def main():
    """My function."""
    sentence_1, sentence_2, count = input(), input(), {}
    for char_1 in sentence_1.lower():
        if char_1 not in ".,!?:;- ":
            count[char_1] = count.get(char_1, 0) + 1
    for char_2 in sentence_2.lower():
        if char_2 not in ".,!?:;- ":
            count[char_2] = count.get(char_2, 0) - 1
    print("NO" if any(count.values()) else "YES")


if __name__ == "__main__":
    main()
