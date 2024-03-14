"""Sets."""


def main():
    """My function."""
    word_1, word_2, word_3 = input().split()
    print("YES" if set(word_1) == set(word_2) == set(word_3) else "NO")


if __name__ == "__main__":
    main()
