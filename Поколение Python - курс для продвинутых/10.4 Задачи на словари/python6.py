"""Dictionaries."""
from sys import stdin


def main():
    """My function."""
    reader, book = (line.strip().title() for line in stdin), {}
    num_n = int(next(reader))
    for _ in range(num_n):
        phone, name = next(reader).split()
        book.setdefault(name, []).append(phone)
    next(reader)
    for man in reader:
        print(*book.get(man, ["абонент не найден"]))


if __name__ == "__main__":
    main()
