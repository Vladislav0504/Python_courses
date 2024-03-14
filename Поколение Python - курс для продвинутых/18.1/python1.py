"""Exam."""


def main():
    """My function."""
    file_name = input()
    with open(file_name, "r", encoding="utf8") as inp:
        print(len(inp.readlines()))


if __name__ == "__main__":
    main()
