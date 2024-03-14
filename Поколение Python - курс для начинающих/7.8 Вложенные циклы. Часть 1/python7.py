"""Loops."""


def main():
    """My function."""
    for i in range(6):
        for k in range(12):
            if 19 * i + 9 * k == 100:
                j = 100 - k - i
                print(f"быков = {i}, коров = {k}, телят = {j}")


if __name__ == "__main__":
    main()
