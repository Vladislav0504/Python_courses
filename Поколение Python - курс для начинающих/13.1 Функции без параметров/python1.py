"""Functions."""


def draw_box() -> None:
    """Star box."""
    height, width = 14, 10
    print("*" * width)
    print("".join(("*", " " * (width - 2), "*\n")) * (height - 2), end="")
    print("*" * width)


def main():
    """My function."""
    draw_box()


if __name__ == "__main__":
    main()
