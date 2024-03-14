"""Sets."""


def main():
    """My function."""
    lst = ["apple", "banana", "cherry", "avocado", "pineapple", "apricot",
           "banana", "avocado", "grapefruit"]
    fruits = set(lst)
    print(*sorted(fruits, reverse=True), sep="\n")


if __name__ == "__main__":
    main()
