"""Hash tables."""
from sys import stdin, stdout


def main():
    """My function."""
    reader, phone_book = (line.split() for line in stdin), {}
    next(reader)
    for operation, number, *name in reader:
        number = int(number)
        if operation == "add":
            phone_book[number] = name[0]
        elif operation == "find":
            result = phone_book.get(number, "not found")
            stdout.write(f"{result}\n")
        else:
            phone_book.pop(number, "not found")


if __name__ == "__main__":
    main()
