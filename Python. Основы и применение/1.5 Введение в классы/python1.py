"""Classes."""


class MoneyBox:
    """MoneyBox."""

    def __init__(self, capacity: int) -> None:
        """Variable self.val is number of coins."""
        self.val = 0
        self.capacity = capacity

    def can_add(self, value: int) -> bool:
        """Is it possible to add value coins?."""
        return self.val + value <= self.capacity

    def add(self, value: int) -> None:
        """Add value coins in moneybox."""
        self.val += value


def main():
    """My function."""
    money_box = MoneyBox(10)
    print(money_box.can_add(11))
    money_box.add(5)
    print(money_box.can_add(4))


if __name__ == "__main__":
    main()
