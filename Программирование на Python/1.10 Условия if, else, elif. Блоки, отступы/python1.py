"""Conditions."""


def main():
    """My function."""
    a_hours = int(input())
    b_hours = int(input())
    hours = int(input())
    if a_hours <= hours <= b_hours:
        print("Это нормально")
    elif hours < a_hours:
        print("Недосып")
    else:
        print("Пересып")


if __name__ == "__main__":
    main()
