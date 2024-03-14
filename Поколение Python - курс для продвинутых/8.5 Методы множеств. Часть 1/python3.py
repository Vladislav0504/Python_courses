"""Sets."""


def main():
    """My function."""
    words = {word.strip(".,;:-?!") for word in input().lower().split()}
    print(len(words))


if __name__ == "__main__":
    main()
