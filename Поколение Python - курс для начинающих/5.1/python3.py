"""Exam."""


def main():
    """My function."""
    age, gender, limits = int(input()), input(), (10, 15)
    print("YES" if limits[0] <= age <= limits[1] and gender == "f" else "NO")


if __name__ == "__main__":
    main()
