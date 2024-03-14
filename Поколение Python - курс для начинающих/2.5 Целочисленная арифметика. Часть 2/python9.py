"""Int function."""


def main():
    """My function."""
    num = list(map(int, input()))
    print(f"Цифра в позиции тысяч равна {num[0]}")
    print(f"Цифра в позиции сотен равна {num[1]}")
    print(f"Цифра в позиции десятков равна {num[2]}")
    print(f"Цифра в позиции единиц равна {num[3]}")


if __name__ == "__main__":
    main()
