"""Files."""


def main():
    """My function."""
    with open("dataset_24465_4.txt", "r", encoding="utf8") as file:
        lst = list(file)
    with open("text1.txt", "w", encoding="utf8") as file:
        file.write("".join(lst[::-1]))


if __name__ == "__main__":
    main()
