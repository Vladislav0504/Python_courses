"""Iterators and generators."""
from itertools import takewhile

from typing import Iterator


def primes() -> Iterator[int]:
    """Prime numbers."""
    prime_nums, number = [], 2
    while number:
        for num in prime_nums:
            if number % num == 0:
                break
        else:
            prime_nums.append(number)
            yield number
        number += 1


def main():
    """My function."""
    print(list(takewhile(lambda x: x <= 31, primes())))
    # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]


if __name__ == "__main__":
    main()
