"""Dictionaries."""


def main() -> dict[str, list[int]]:
    """My function."""
    words = ["hello", "bye", "yes", "no", "python", "apple", "maybe", "stepik",
             "beegeek"]
    return {word: list(map(ord, word)) for word in words}


if __name__ == "__main__":
    result = main()
    print(result)
