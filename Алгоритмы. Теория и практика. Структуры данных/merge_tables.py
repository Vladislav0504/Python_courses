"""Disjoint sets."""
from sys import stdin, stdout


class DisjointSets:
    """Disjoint sets."""

    def __init__(self, sizes: list[int]) -> None:
        """Disjoint sets' constructor."""
        self.parent = list(range(len(sizes) + 1))
        self.rank = [0] * (len(sizes) + 1)
        self.size = [0, *sizes]

    def find(self, i: int) -> int:
        """Find leader."""
        if i != self.parent[i]:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        """Union of sets."""
        i, j = self.find(i), self.find(j)
        if i != j:
            if self.rank[i] < self.rank[j]:
                i, j = j, i
            if self.rank[i] == self.rank[j]:
                self.rank[i] += 1
            self.size[i] += self.size[j]
            self.size[j], self.parent[j] = 0, i


def main():
    """My function."""
    reader = (map(int, line.split()) for line in stdin)
    next(reader)
    array_r = list(next(reader))
    sets, maximum = DisjointSets(array_r), max(array_r)
    for destination, source in reader:
        sets.union(destination, source)
        maximum = max(maximum, sets.size[sets.find(destination)])
        stdout.write(f"{maximum}\n")


if __name__ == "__main__":
    main()
