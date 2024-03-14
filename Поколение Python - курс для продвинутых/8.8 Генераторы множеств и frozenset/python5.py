"""Sets."""


def main():
    """My function."""
    files = ["python.png", "qwerty.py", "stepik.png", "beegeek.org",
             "windows.pnp", "pen.txt", "phone.py", "book.txT", "board.pNg",
             "keyBoard.jpg", "Python.PNg", "apple.jpeg", "png.png",
             "input.tXt", "split.pop", "solution.Py", "stepik.org",
             "kotlin.ko", "github.git"]
    result = {file for file in map(str.lower, files) if file.endswith(".png")}
    print(*sorted(result))


if __name__ == "__main__":
    main()
