"""Types."""


def main():
    """My function."""
    num_a, num_b, num_c = (float(input()) for _ in range(3))
    discriminant = num_b**2 - 4 * num_a * num_c
    if discriminant < 0:
        print("Нет корней")
    elif discriminant == 0:
        print(-num_b / (2 * num_a))
    else:
        root_1 = (-num_b + discriminant**0.5) / (2 * num_a)
        root_2 = (-num_b - discriminant**0.5) / (2 * num_a)
        print(*sorted((root_1, root_2)), sep="\n")


if __name__ == "__main__":
    main()
