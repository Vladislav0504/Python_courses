"""Int function."""


def main():
    """My function."""
    num_a, num_b = int(input()), int(input())
    k = [3, 275, -127, -41]
    num_f = k[0] * (num_a + num_b)**3 + k[1] * num_b**2 + k[2] * num_a + k[3]
    print(num_f)


if __name__ == "__main__":
    main()
