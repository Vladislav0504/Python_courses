"""Exam."""


def draw_triangle() -> None:
    """Star triangle."""
    base, height = 15, 8
    print(*("".join((" " * ((base >> 1) - i), "*" * ((i << 1) + 1)))
            for i in range(height)), sep="\n")


def main():
    """My function."""
    draw_triangle()


if __name__ == "__main__":
    main()
