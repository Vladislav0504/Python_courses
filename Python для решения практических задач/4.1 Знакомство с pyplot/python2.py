"""Pyplot."""
from numpy import sin, cos, arange

from matplotlib import rcParams

import matplotlib.pyplot as plt


def main():
    """My function."""
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))  # создаем график
    rcParams.update({"font.size": 10})
    # на оси x будет изображаться участок от 0 до 10, а на оси y от -1.5 до 1.5
    plt.axis((0, 10, -1.5, 1.5))

    plt.title("Sine & Cosine")
    plt.xlabel("x")  # подпись оси x
    plt.ylabel("F(x)")  # подпись оси y

    x_vals = arange(0, 10, 0.1)  # x-координаты точек

    # создаем графики: первый аргумент - x-координаты, второй - y-координаты
    plt.plot(x_vals, sin(x_vals), color="blue", linestyle="solid",
             label="sin(x)")
    plt.plot(x_vals, cos(x_vals), color="red", linestyle="dashed",
             label="cos(x)")

    plt.legend(loc="lower left")
    plt.show()
    fig.savefig("trigonometry2.png")  # сохраняем график в файл


if __name__ == "__main__":
    main()
