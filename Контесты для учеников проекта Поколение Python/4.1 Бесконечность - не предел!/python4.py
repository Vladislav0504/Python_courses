"""Contest."""


def main():
    """My function."""
    num_n = input()
    for i, char in enumerate(num_n):
        if char == "6":
            print("".join((num_n[:i], "9", num_n[i + 1:])))
            break
    else:
        print(num_n)


if __name__ == "__main__":
    main()
