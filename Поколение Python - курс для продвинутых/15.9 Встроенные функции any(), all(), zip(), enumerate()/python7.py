"""Functions."""
from sys import stdin


def main():
    """My function."""
    reader = (line.strip() for line in stdin)
    num_n, lst = int(next(reader)), []
    for _ in range(num_n):
        num_k = int(next(reader))
        lst.append(tuple(int(next(reader).split()[1]) for _ in range(num_k)))
    print("YES" if all(any(map(lambda x: x == 5, cl)) for cl in lst) else "NO")


if __name__ == "__main__":
    main()
