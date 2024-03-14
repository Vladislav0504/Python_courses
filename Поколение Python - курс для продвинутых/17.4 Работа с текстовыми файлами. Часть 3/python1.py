"""Files."""


def main():
    """My function."""
    text = input()
    with open("output.txt", "w", encoding="utf8") as out:
        out.write(text)


if __name__ == "__main__":
    main()
