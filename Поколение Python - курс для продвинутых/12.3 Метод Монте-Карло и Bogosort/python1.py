"""Monte-Carlo method."""
from random import uniform


def main():
    """My function."""
    num_n, num_k, left, right = 10**6, 0, -2, 2
    square = (right - left)**2
    for _ in range(num_n):
        num_x, num_y = uniform(left, right), uniform(left, right)
        if num_x**3 + num_y**4 + 2 >= 0 and 3 * num_x + num_y**2 <= 2:
            num_k += 1
    result = num_k * square / num_n
    print(result)


if __name__ == "__main__":
    main()
