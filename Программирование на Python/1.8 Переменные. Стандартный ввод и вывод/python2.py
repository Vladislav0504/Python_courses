"""Variables."""


def main():
    """My function."""
    minutes_per_hour = 60
    x_minutes = int(input())
    print(*divmod(x_minutes, minutes_per_hour), sep="\n")


if __name__ == "__main__":
    main()
