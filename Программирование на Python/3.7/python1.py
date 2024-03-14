"""Problems."""


def main():
    """My function."""
    num_n, table = int(input()), {}
    for _ in range(num_n):
        line = input().split(";")
        line[1], line[3] = int(line[1]), int(line[3])
        for j in (0, 2):
            values = table.setdefault(line[j], [0, 0, 0, 0, 0])
            values[0] += 1
            values[1] += line[j + 1] > line[j - 1]
            values[2] += line[j + 1] == line[j - 1]
    for key, value in table.items():
        value[3] = value[0] - value[1] - value[2]
        value[4] = value[1] * 3 + value[2]
        print(f"{key}:", *value)


if __name__ == "__main__":
    main()
