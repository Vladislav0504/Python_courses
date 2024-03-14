"""Classes."""


class Buffer:
    """Buffer."""

    def __init__(self) -> None:
        """Elements in list."""
        self.lst = []

    def add(self, *nums: int) -> None:
        """Add elements."""
        for num in nums:
            self.lst.append(num)
            if len(self.lst) == 5:
                print(sum(self.lst))
                self.lst.clear()

    def get_current_part(self) -> list[int]:
        """Return sequence elements."""
        return self.lst


def main():
    """My function."""
    buf = Buffer()
    buf.add(1, 2, 3)
    print(buf.get_current_part())  # вернуть [1, 2, 3]
    buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
    print(buf.get_current_part())  # вернуть [6]
    buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
    print(buf.get_current_part())  # вернуть []
    buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)  # print(5), print(5)
    print(buf.get_current_part())  # вернуть [1]


if __name__ == "__main__":
    main()
