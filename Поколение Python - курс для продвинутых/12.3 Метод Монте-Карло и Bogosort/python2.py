"""Monte-Carlo method."""
from random import uniform


def main():
    """My function."""
    num_n, num_k, left, right = 10**6, 0, -1, 1
    square = (right - left)**2
    for _ in range(num_n):
        num_x, num_y = uniform(left, right), uniform(left, right)
        if num_x**2 + num_y**2 <= 1:
            num_k += 1
    num_pi = num_k * square / num_n
    print(num_pi)


if __name__ == "__main__":
    main()
