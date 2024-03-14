"""Contest."""


def main():
    """My function."""
    str_a, str_b = input(), input()
    diff = {}
    for char_b in str_b:
        diff[char_b] = diff.get(char_b, 0) + 1
    for char_a in str_a:
        diff[char_a] -= 1
    print("".join(ch * count for ch, count in diff.items()))


if __name__ == "__main__":
    main()
