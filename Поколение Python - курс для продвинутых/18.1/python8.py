"""Exam."""


def main():
    """My function."""
    file_name, lst = input(), []
    with open(file_name, "r", encoding="utf8") as inp:
        lines = inp.readlines()
        for i, line in enumerate(lines):
            if line.startswith("def ") and lines[max(0, i - 1)][0] != "#":
                lst.append(line[4:line.index("(")])
        print(*lst if lst else ("Best Programming Team",), sep="\n")


if __name__ == "__main__":
    main()
