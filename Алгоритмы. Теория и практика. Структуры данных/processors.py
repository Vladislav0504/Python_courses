"""Priority queue.

Good program.
"""
from sys import stdout


class PriorityQueue:
    """PriorityQueue."""

    def __init__(self, array: list[(int, int)] = None) -> None:
        """Heap constructor."""
        self.lst = array or []

    def get_min(self) -> (int, int):
        """Get minimum."""
        return self.lst[0]

    def change_priority(self, pair: (int, int)) -> None:
        """Change priority."""
        self.lst[0] = pair
        self.__sift_down(0)

    def __sift_down(self, i: int) -> None:
        """Sift down index i."""
        j = (i << 1) + 1
        while j < len(self.lst):
            k = j + 1
            if k < len(self.lst) and self.lst[j] > self.lst[k]:
                j = k
            if self.lst[i] <= self.lst[j]:
                break
            self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
            i = j
            j = (i << 1) + 1


def main():
    """My function."""
    num_n, num_m = map(int, input().split())
    array_t = list(map(int, input().split()))
    heap = PriorityQueue([(0, i) for i in range(min(num_n, num_m))])
    for t_i in array_t:
        time, processor = heap.get_min()
        stdout.write(f"{processor} {time}\n")
        heap.change_priority((time + t_i, processor))


if __name__ == "__main__":
    main()
