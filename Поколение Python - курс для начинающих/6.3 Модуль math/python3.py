"""Types."""


def main():
    """My function."""
    num_a, num_b = float(input()), float(input())
    arithmetic_m = (num_a + num_b) / 2
    geometric_m = (num_a * num_b)**0.5
    harmonic_m = 2 * num_a * num_b / (num_a + num_b)
    quadratic_m = ((num_a**2 + num_b**2) / 2)**0.5
    print(arithmetic_m, geometric_m, harmonic_m, quadratic_m, sep="\n")


if __name__ == "__main__":
    main()
