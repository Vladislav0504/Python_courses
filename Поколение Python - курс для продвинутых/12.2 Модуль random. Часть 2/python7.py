"""Random."""
from random import shuffle

from sys import stdin


def main():
    """My function."""
    num_n, lst = int(input()), [line.strip() for line in stdin]
    lst_2 = lst.copy()
    shuffle(lst_2)
    pairs = {lst_2[i - 1]: lst_2[i] for i in range(num_n)}
    print(*(f"{student} - {pairs[student]}" for student in lst), sep="\n")


if __name__ == "__main__":
    main()
