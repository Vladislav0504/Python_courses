"""Basic data structures."""
from sys import stdout

from collections import deque


def main():
    """My function."""
    _, array_a = input(), list(map(int, input().split()))
    num_m, queue = int(input()), deque()
    for i, num in enumerate(array_a):
        if i >= num_m and array_a[i - num_m] == queue[0]:
            queue.popleft()
        while queue and queue[-1] < num:
            queue.pop()
        queue.append(num)
        if i + 1 >= num_m:
            stdout.write(f"{queue[0]} ")


if __name__ == "__main__":
    main()
