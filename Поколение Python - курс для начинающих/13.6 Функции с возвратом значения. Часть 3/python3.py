"""Functions."""


def solve(num_a: int, num_b: int, num_c: int) -> (float, float):
    """Roots of quadratic equation."""
    discriminant = num_b**2 - (num_a * num_c << 2)
    root_1 = (-num_b + discriminant**0.5) / (num_a << 1)
    root_2 = (-num_b - discriminant**0.5) / (num_a << 1)
    return min(root_1, root_2), max(root_1, root_2)


def main():
    """My function."""
    num_a, num_b, num_c = (int(input()) for _ in range(3))
    x_1, x_2 = solve(num_a, num_b, num_c)
    print(x_1, x_2)


if __name__ == "__main__":
    main()
