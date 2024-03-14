"""Problems."""


def main():
    """My function."""
    num = int(input())
    bounds = (-15, 12, 14, 17, 19)
    print(bounds[0] < num <= bounds[1] or bounds[2] < num < bounds[3]
          or bounds[4] <= num)


if __name__ == "__main__":
    main()
