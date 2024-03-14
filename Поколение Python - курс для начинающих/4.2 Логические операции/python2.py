"""Conditions."""


def main():
    """My function."""
    num_x = int(input())
    print("Принадлежит" if num_x <= -3 or num_x >= 7 else "Не принадлежит")


if __name__ == "__main__":
    main()
