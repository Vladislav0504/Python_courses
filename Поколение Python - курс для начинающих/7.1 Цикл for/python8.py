"""Loops."""


def main():
    """My function."""
    num_m, num_p, num_n = (int(input()) for _ in range(3))
    for i in range(num_n):
        print(i + 1, num_m * (1 + num_p / 100)**i)


if __name__ == "__main__":
    main()
