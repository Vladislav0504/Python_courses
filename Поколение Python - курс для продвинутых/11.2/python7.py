"""Exam."""
from sys import stdin, stdout


def main():
    """My function."""
    _, data = input(), {}
    for line in stdin:
        buyer, goods, total = line.split()
        my_dict = data.setdefault(buyer, {})
        my_dict[goods] = my_dict.get(goods, 0) + int(total)
    for name, products in sorted(data.items()):
        stdout.write(f"{name}:\n")
        for product, number in sorted(products.items()):
            stdout.write(f"{product} {number}\n")


if __name__ == "__main__":
    main()
