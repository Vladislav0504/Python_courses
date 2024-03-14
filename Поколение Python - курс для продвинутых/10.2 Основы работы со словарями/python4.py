"""Dictionaries."""


def main():
    """My function."""
    numbers = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
               6: "six", 7: "seven", 8: "eight", 9: "nine"}
    number = input()
    print(*(numbers[num] for num in map(int, number)))


if __name__ == "__main__":
    main()
