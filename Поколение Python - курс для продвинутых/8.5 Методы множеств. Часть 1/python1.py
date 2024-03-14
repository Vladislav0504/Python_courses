"""Sets."""
from sys import stdin


def main():
    """My function."""
    input()
    print(*(len(set(word.strip().lower())) for word in stdin), sep="\n")


if __name__ == "__main__":
    main()
