"""Contest."""


def main():
    """My function."""
    minutes, lesson, break_time, first = 60, 45, 5, 8
    num_n = int(input())
    minutes_time = first * minutes + num_n * lesson + (num_n - 1) * break_time
    print(*divmod(minutes_time, minutes))


if __name__ == "__main__":
    main()
