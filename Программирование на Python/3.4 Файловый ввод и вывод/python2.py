"""Files."""


def main():
    """My function."""
    words = {}
    with open("dataset_3363_3.txt", "r", encoding="utf8") as file:
        for line in file:
            for word in line.strip().lower().split():
                words[word] = words.get(word, 0) + 1
    max_key, max_value = "", 0
    for key, value in words.items():
        if value > max_value or value == max_value and max_key > key:
            max_key, max_value = key, value
    with open("text2.txt", "w", encoding="utf8") as file:
        file.write(f"{max_key} {max_value}")


if __name__ == "__main__":
    main()
