"""Binary search trees."""
from sys import stdin


def main():
    """My function."""
    string = stdin.readline().strip()
    reader = (map(int, line.split()) for line in stdin)
    next(reader)
    for i, j, k in reader:
        ends = string[:i] + string[j + 1:]
        string = ends[:k] + string[i:j + 1] + ends[k:]
    print(string)


if __name__ == "__main__":
    main()
