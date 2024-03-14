"""Disjoint sets.

Good program.
"""
from sys import stdin


class DisjointSets:
    """Disjoint sets."""

    def __init__(self, size: int) -> None:
        """Disjoint sets' constructor."""
        self.parent = list(range(size + 1))
        self.rank = [0] * (size + 1)

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
            self.parent[j] = i


def main():
    """My function."""
    reader = (map(int, line.split()) for line in stdin)
    num_n, num_e, _ = next(reader)
    sets = DisjointSets(num_n)
    for k, (i, j) in enumerate(reader):
        if k < num_e:
            sets.union(i, j)
        elif sets.find(i) == sets.find(j):
            print(0)
            break
    else:
        print(1)


if __name__ == "__main__":
    main()
