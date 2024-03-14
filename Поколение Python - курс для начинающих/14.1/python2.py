"""Exam."""


def get_shipping_cost(quantity: int) -> int:
    """Shipping cost."""
    cost_1, cost_2 = 1000, 120
    return cost_1 + (quantity - 1) * cost_2


def main():
    """My function."""
    num = int(input())
    print(get_shipping_cost(num))


if __name__ == "__main__":
    main()
