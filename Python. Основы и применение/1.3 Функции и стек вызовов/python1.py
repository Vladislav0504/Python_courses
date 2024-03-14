"""Functions."""


def closest_mod_5(num_x: int) -> int:
    """Closest number divisible by 5."""
    return num_x + (-num_x) % 5


def main():
    """My function."""
    print(closest_mod_5(7))


if __name__ == "__main__":
    main()
