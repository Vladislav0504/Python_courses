"""Hash tables.

Good program.
"""
from sys import stdin, stdout


class HashTable:
    """HashTable."""

    prime, num_x = 1000000007, 263

    def __init__(self, size: int) -> None:
        """Hash table constructor."""
        self.table = [[] for _ in range(size)]

    def hash(self, string: str) -> int:
        """Hash function."""
        k = ord(string[-1])
        for char in string[-2::-1]:
            k = (k * self.num_x + ord(char)) % self.prime
        return k % len(self.table)

    def add(self, string: str) -> None:
        """Add string."""
        lst = self.table[self.hash(string)]
        if string not in lst:
            lst.append(string)

    def delete(self, string: str) -> None:
        """Delete string."""
        lst = self.table[self.hash(string)]
        if string in lst:
            lst.remove(string)

    def find(self, string: str) -> str:
        """Find string."""
        lst = self.table[self.hash(string)]
        return "yes" if string in lst else "no"

    def check(self, i: int) -> str:
        """Check self.table[i]."""
        return " ".join(self.table[i][::-1])


def main():
    """My function."""
    hash_table, _ = HashTable(int(input())), input()
    for line in stdin:
        operation, arg = line.split()
        if operation == "add":
            hash_table.add(arg.rstrip())
        elif operation == "find":
            result = hash_table.find(arg.rstrip())
            stdout.write(f"{result}\n")
        elif operation == "check":
            result = hash_table.check(int(arg))
            stdout.write(f"{result}\n")
        else:
            hash_table.delete(arg.rstrip())


if __name__ == "__main__":
    main()
