"""Problems."""


def main():
    """My function."""
    num_n = input()
    if num_n[-1] in "567890" or num_n[-2:] in ("11", "12", "13", "14"):
        print(num_n, "программистов")
    elif num_n[-1] in "234":
        print(num_n, "программиста")
    else:
        print(num_n, "программист")


if __name__ == "__main__":
    main()
