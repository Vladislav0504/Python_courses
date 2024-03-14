"""Functions."""


def draw_triangle() -> None:
    """Star triangle."""
    height = 10
    print(*("*" * i for i in range(1, height + 1)), sep="\n")


def main():
    """My function."""
    draw_triangle()


if __name__ == "__main__":
    main()
