"""Files."""
from sys import stdin


def main():
    """My function."""
    reader = (line.strip() for line in stdin)
    next(reader)
    with open("output.txt", "w", encoding="utf8") as out:
        for file_name in reader:
            with open(file_name, "r", encoding="utf8") as inp:
                out.write(inp.read())


if __name__ == "__main__":
    main()
