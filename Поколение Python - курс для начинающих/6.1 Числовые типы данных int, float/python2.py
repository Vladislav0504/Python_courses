"""Types."""


def main():
    """My function."""
    distance, v_1, v_2 = (float(input()) for _ in range(3))
    print(distance / (v_1 + v_2))


if __name__ == "__main__":
    main()
