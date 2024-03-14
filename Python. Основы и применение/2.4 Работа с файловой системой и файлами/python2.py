"""Files."""
from os import walk


def main():
    """My function."""
    with open("text2.txt", "w", encoding="utf8") as file:
        for current_dir, _, files in walk("main"):
            if any(f.endswith(".py") for f in files):
                file.write(f"{current_dir}\n")


if __name__ == "__main__":
    main()
