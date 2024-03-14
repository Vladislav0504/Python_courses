"""Problems."""


def main():
    """My function."""
    num_n, coord = int(input()), [0, 0]
    directions = {"север": (0, 1), "запад": (-1, 0), "юг": (0, -1),
                  "восток": (1, 0)}
    for _ in range(num_n):
        direction, distance = input().split()
        for i in (0, 1):
            coord[i] += directions[direction][i] * int(distance)
    print(*coord)


if __name__ == "__main__":
    main()
