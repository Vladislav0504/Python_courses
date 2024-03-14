"""Pyplot."""
from numpy import array

from matplotlib import rcParams

import matplotlib.pyplot as plt


def main():
    """My function."""
    data_names = ["cafe", "pharmacy", "fuel", "bank", "waste_disposal",
                  "atm", "bench", "parking", "restaurant", "place_of_worship"]
    data_values = array([9124, 8652, 7592, 7515, 7041, 6487, 6374, 6277,
                         5092, 3629])

    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(1024 / dpi, 768 / dpi))
    rcParams.update({"font.size": 10})

    plt.title("OpenStreetMap Point Types")

    axes = plt.axes()
    axes.yaxis.grid(True, zorder=1)  # True - показать линии сетки,
    # чем больше zorder, тем на более ближнем плане график
    x_vals = array(range(len(data_names)))

    plt.bar(x_vals + 0.05, 0.9 * data_values, width=0.2, color="red",
            alpha=0.7, label="2016", zorder=2)
    plt.bar(x_vals + 0.3, data_values, width=0.2, color="blue",
            alpha=0.7, label="2017", zorder=2)
    plt.xticks(x_vals, data_names)  # названия data_names для точек x_vals

    fig.autofmt_xdate(rotation=25)  # вращение меток xtick на 25 градусов

    plt.legend(loc="upper right")
    plt.show()
    fig.savefig("bars.png")  # сохраняем график в файл


if __name__ == "__main__":
    main()
