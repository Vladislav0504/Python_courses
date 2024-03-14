"""Types."""


def main():
    """My function."""
    age, delta = int(input()), (10.5, 4)
    print(min(age, 2) * delta[0] + max(0, age - 2) * delta[1])


if __name__ == "__main__":
    main()
