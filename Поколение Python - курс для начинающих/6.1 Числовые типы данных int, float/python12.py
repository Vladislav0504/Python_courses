"""Types."""


def main():
    """My function."""
    p_1, p_2, q_1, q_2 = (int(input()) for _ in range(4))
    print(abs(p_1 - q_1) + abs(p_2 - q_2))


if __name__ == "__main__":
    main()
