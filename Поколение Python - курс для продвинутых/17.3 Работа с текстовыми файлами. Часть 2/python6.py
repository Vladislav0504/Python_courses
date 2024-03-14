"""Files."""


def main():
    """My function."""
    print("Input file contains:")
    with open("file.txt", "r", encoding="utf8") as inp:
        lines = inp.readlines()
        my_dict = {"letters": 0, "words": 0, "lines": len(lines)}
        for line in lines:
            my_dict["words"] += len(line.split())
            my_dict["letters"] += sum(map(str.isalpha, line))
        print(*(f"{value} {key}" for key, value in my_dict.items()), sep="\n")


if __name__ == "__main__":
    main()
