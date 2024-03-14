"""Functions."""


def draw_triangle(fill: str, base: int) -> None:
    """Triangle."""
    print(*(fill * min(i + 1, base - i) for i in range(base)), sep="\n")


def main():
    """My function."""
    fill, base = input(), int(input())
    draw_triangle(fill, base)


if __name__ == "__main__":
    main()
