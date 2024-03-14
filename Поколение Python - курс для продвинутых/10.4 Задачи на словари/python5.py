"""Dictionaries."""
from sys import stdin


def main():
    """My function."""
    reader, dictionary = (line.strip() for line in stdin), {}
    num_n = int(next(reader))
    for _ in range(num_n):
        country, *cities = next(reader).split()
        dictionary.update(dict.fromkeys(cities, country))
    next(reader)
    print(*(dictionary[city] for city in reader), sep="\n")


if __name__ == "__main__":
    main()
