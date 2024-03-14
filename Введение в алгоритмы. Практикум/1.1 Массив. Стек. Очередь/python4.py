"""Array. Stack. Queue."""
from sys import stdin, stdout


class Queue:
    """Queue."""

    def __init__(self) -> None:
        """Queue constructor."""
        self.inp = []
        self.out = []

    def __len__(self) -> int:
        """Length."""
        return len(self.inp) + len(self.out)

    def push(self, num: int) -> None:
        """Push."""
        self.inp.append(num)

    def pop(self) -> int:
        """Pop."""
        if not self.out:
            self.inp.reverse()
            self.inp, self.out = self.out, self.inp
        return self.out.pop()


def main():
    """My function."""
    queue = Queue()
    for line in stdin:
        line = line.strip()
        if line == "+":
            if queue:
                number = queue.pop()
                stdout.write(f"{number}\n")
        elif line and len(queue) <= 4:
            queue.push(int(line))


if __name__ == "__main__":
    main()
