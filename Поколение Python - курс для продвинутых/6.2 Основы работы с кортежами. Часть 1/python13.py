"""Tuples."""


def main():
    """My function."""
    tuples = [(10, 20, 40), (40, 50, 60), (70, 80, 90), (10, 90), (1, 2, 3, 4),
              (5, 6, 10, 2, 1, 77)]
    new_tuples = [elem[:-1] + (100,) for elem in tuples]
    print(new_tuples)


if __name__ == "__main__":
    main()
