"""Files."""


def main():
    """My function."""
    with open("goats.txt", "r", encoding="utf8") as inp:
        text = inp.read().split("\n")
        index_goats = text.index("GOATS")
        colours = dict.fromkeys(text[1:index_goats], 0)
        for colour in text[index_goats + 1:]:
            colours[colour] += 1
    total, limit = len(text[index_goats + 1:]), 0.07
    with open("answer.txt", "w", encoding="utf8") as out:
        print(*sorted(col for col, k in colours.items() if k > total * limit),
              sep="\n", file=out)


if __name__ == "__main__":
    main()
