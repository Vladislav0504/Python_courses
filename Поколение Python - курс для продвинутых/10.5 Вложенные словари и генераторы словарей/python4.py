"""Dictionaries."""


def main() -> dict[str, int]:
    """My function."""
    months = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May",
              6: "June", 7: "July", 8: "August", 9: "September", 10: "October",
              11: "November", 12: "December"}
    return {value: key for key, value in months.items()}


if __name__ == "__main__":
    result = main()
    print(result)
