"""Greedy algorithms.

Good program.
"""
from sys import stdin, stdout


class PriorityQueue:
    """PriorityQueue."""

    lst = []

    def insert(self, num_x: int) -> None:
        """Insert num_x."""
        self.lst.append(num_x)
        self.__sift_up(len(self.lst) - 1)

    def extract_min(self) -> int:
        """Extract minimum."""
        self.lst[0], self.lst[-1] = self.lst[-1], self.lst[0]
        self.__sift_down(0, len(self.lst) - 1)
        return self.lst.pop()

    def __sift_up(self, i: int) -> None:
        """Sift up index i."""
        k = i - 1 >> 1
        while i and self.lst[i] < self.lst[k]:
            self.lst[i], self.lst[k] = self.lst[k], self.lst[i]
            i = k
            k = i - 1 >> 1

    def __sift_down(self, i: int, length: int) -> None:
        """Sift down index i."""
        j = (i << 1) + 1
        while j < length:
            k = j + 1
            if k < length and self.lst[j] > self.lst[k]:
                j = k
            if self.lst[i] <= self.lst[j]:
                break
            self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
            i = j
            j = (i << 1) + 1


def main():
    """My function."""
    input()
    priority_queue = PriorityQueue()
    for line in stdin:
        operation, *num_x = line.split()
        if operation == "Insert":
            priority_queue.insert(-int(num_x[0]))
        else:
            max_number = -priority_queue.extract_min()
            stdout.write(f"{max_number}\n")


if __name__ == "__main__":
    main()
