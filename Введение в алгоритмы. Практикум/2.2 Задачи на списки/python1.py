"""List."""
from sys import stdin, stdout

from collections import deque


def main():
    """My function."""
    input()
    deque_1, deque_2 = deque(), deque()
    for line in stdin:
        if line[0] == "+":
            number = deque_1.popleft()
            stdout.write(f"{number}\n")
        elif line[0] == "i":
            deque_2.appendleft(int(line.split()[1]))
        elif line[0] == "s":
            deque_2.append(int(line.split()[1]))
        if len(deque_1) < len(deque_2):
            deque_1.append(deque_2.popleft())


if __name__ == "__main__":
    main()
