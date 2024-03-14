"""Functions."""
from sys import stdout


def main():
    """My function."""
    countries = ["Russia", "USA", "UK", "Germany", "France", "India"]
    capitals = ["Moscow", "Washington", "London", "Berlin", "Paris", "Delhi"]
    populations = [145_934_462, 331_002_651, 80_345_321, 67_886_011,
                   65_273_511, 1_380_004_385]
    for capital, country, population in zip(capitals, countries, populations):
        stdout.write(f"{capital} is the capital of {country},"
                     f" population equal {population} people.\n")


if __name__ == "__main__":
    main()
