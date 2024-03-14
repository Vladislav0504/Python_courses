"""Types."""


def main():
    """My function."""
    n_1, n_2, n_3 = sorted(map(int, input()))
    print("Число интересное" if n_3 - n_1 == n_2 else "Число неинтересное")


if __name__ == "__main__":
    main()
