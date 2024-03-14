"""Sets."""
from sys import stdout


def main():
    """My function."""
    numbers = set()
    for num in map(int, input().split()):
        stdout.write("YES\n" if num in numbers else "NO\n")
        numbers.add(num)


if __name__ == "__main__":
    main()
