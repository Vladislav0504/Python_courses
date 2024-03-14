"""Basic data structures."""
from sys import stdin, stdout

from collections import deque


class Processor:
    """Processor."""

    def __init__(self, size: int) -> None:
        """Processor constructor."""
        self.size = size
        self.queue = deque()

    def __repr__(self) -> str:
        """Representation."""
        queue, size = repr(self.queue), repr(self.size)
        return f"queue = {queue}, size = {size}"

    def push(self, arrival: int, duration: int) -> int:
        """Push."""
        while self.queue and self.queue[0] <= arrival:
            self.queue.popleft()
        if len(self.queue) < self.size:
            start = max(self.queue[-1] if self.queue else 0, arrival)
            self.queue.append(start + duration)
            return start
        return -1


def main():
    """My function."""
    reader = (map(int, line.split()) for line in stdin)
    size, _ = next(reader)
    queue = Processor(size)
    for arrival, duration in reader:
        result = queue.push(arrival, duration)
        stdout.write(f"{result}\n")


if __name__ == "__main__":
    main()
