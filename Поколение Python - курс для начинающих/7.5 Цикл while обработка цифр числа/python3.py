"""Loops."""


def main():
    """My function."""
    num = input()
    max_num, min_num = max(map(int, num)), min(map(int, num))
    print(f"Максимальная цифра равна {max_num}")
    print(f"Минимальная цифра равна {min_num}")


if __name__ == "__main__":
    main()
