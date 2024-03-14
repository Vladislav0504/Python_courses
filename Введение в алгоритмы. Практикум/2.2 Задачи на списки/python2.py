"""List."""
from sys import stdin, stdout

from collections import deque


def main():
    """My function."""
    input()
    deque_1, deque_2 = deque(), deque()
    push = {"c": deque_1.appendleft,
            "i": deque_2.appendleft,
            "s": deque_2.append}
    for line in stdin:
        if line[0] == "+":
            number = deque_1.popleft()
            stdout.write(f"{number}\n")
        elif line[0] in "cis":
            push[line[0]](int(line.split()[1]))
        if len(deque_1) < len(deque_2):
            deque_1.append(deque_2.popleft())
        elif len(deque_1) == len(deque_2) + 2:
            deque_2.appendleft(deque_1.pop())


if __name__ == "__main__":
    main()
