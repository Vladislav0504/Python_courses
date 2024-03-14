"""Files."""


def main():
    """My function."""
    num, cur_char = 0, ""
    with open("dataset_3363_2.txt", "r", encoding="utf8") as inp:
        with open("text1.txt", "w", encoding="utf8") as out:
            for char in f"{inp.readline()}a":
                if char.isdigit():
                    num = 10 * num + int(char)
                else:
                    out.write(cur_char * num)
                    cur_char, num = char, 0


if __name__ == "__main__":
    main()
