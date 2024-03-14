"""Sets."""


def main():
    """My function."""
    words = ["Plum", "Grapefruit", "apple", "orange", "pomegranate",
             "Cranberry", "lime", "Lemon", "grapes", "persimmon", "tangerine",
             "Watermelon", "currant", "Almond"]
    my_set = {word[0].lower() for word in words}
    print(*sorted(my_set))


if __name__ == "__main__":
    main()
