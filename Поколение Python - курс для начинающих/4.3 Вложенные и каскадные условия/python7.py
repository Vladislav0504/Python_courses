"""Conditions."""


def main():
    """My function."""
    col_1, col_2 = sorted((input(), input()))
    colors = ("желтый", "красный", "синий")
    mix = {("красный", "синий"): "фиолетовый", ("желтый", "синий"): "зеленый",
           ("желтый", "красный"): "оранжевый"}
    if col_1 not in colors or col_2 not in colors:
        print("ошибка цвета")
    else:
        print(mix.get((col_1, col_2), col_1))


if __name__ == "__main__":
    main()
