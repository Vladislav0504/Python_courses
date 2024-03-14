"""Strings."""


def main():
    """My function."""
    string, count = input(), {}
    for i, char in enumerate(string):
        count.setdefault(char, [0, i])
        count[char][0] += 1
        count[char][1] = i
    print(max(count, key=lambda k: count[k], default=""))


if __name__ == "__main__":
    main()
