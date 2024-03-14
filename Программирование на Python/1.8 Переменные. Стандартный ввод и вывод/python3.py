"""Variables."""


def main():
    """My function."""
    minutes_per_hour = 60
    x_minutes, hours, minutes = int(input()), int(input()), int(input())
    total_minutes = hours * minutes_per_hour + minutes + x_minutes
    print(*divmod(total_minutes, minutes_per_hour), sep="\n")


if __name__ == "__main__":
    main()
