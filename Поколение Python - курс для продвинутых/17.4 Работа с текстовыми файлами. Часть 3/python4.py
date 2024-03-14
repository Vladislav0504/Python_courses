"""Files."""


def main():
    """My function."""
    with open("class_scores.txt", "r", encoding="utf8") as inp:
        with open("new_scores.txt", "w", encoding="utf8") as out:
            limit, reader = 100, (line.split() for line in inp)
            for last_name, mark in reader:
                new_mark = min(limit, int(mark) + 5)
                out.write(f"{last_name} {new_mark}\n")


if __name__ == "__main__":
    main()
