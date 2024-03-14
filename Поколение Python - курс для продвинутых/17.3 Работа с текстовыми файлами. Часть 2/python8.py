"""Files."""
from sys import stdout


def main():
    """My function."""
    with open("population.txt", "r", encoding="utf8") as inp:
        reader, limit = (line.split("\t") for line in inp), 500000
        for country, population in reader:
            if country[0] == "G" and int(population) > limit:
                stdout.write(f"{country}\n")


if __name__ == "__main__":
    main()
