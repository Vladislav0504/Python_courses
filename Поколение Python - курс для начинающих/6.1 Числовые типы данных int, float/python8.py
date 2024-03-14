"""Types."""


def main():
    """My function."""
    lst = [int(input()) for _ in range(5)]
    minimum, maximum = min(lst), max(lst)
    print(f"Наименьшее число = {minimum}")
    print(f"Наибольшее число = {maximum}")


if __name__ == "__main__":
    main()
