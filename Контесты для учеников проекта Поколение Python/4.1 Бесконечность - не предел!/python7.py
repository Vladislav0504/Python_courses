"""Contest."""


def main():
    """My function."""
    string, chars = input(), {}
    result = 0
    for char in string:
        chars[char] = chars.get(char, 0) + 1
    flag = 0
    for value in chars.values():
        result += value
        if value & 1:
            result -= 1
            flag = 1
    print(result + flag)


if __name__ == "__main__":
    main()
