"""Repetition."""


def main():
    """My function."""
    string = input().split("О")
    print(max(map(len, string)))


if __name__ == "__main__":
    main()
