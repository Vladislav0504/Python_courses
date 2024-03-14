"""Exam."""
from sys import stdout


def main():
    """My function."""
    words, my_dict = input().split(), {}
    for word in words:
        k = my_dict[word] = my_dict.get(word, 0) + 1
        stdout.write(f"{k} ")


if __name__ == "__main__":
    main()
