"""Random."""
from random import sample


def main():
    """My function."""
    tickets_number, min_num, max_num = 100, 1000000, 9999999
    print(*sample(range(min_num, max_num + 1), tickets_number), sep="\n")


if __name__ == "__main__":
    main()
