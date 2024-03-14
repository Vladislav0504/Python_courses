"""Array. Stack. Queue."""


def main():
    """My function."""
    array_a, stack = list(map(int, input().split())), []
    array = [-1] * len(array_a)
    for i, num_a in enumerate(array_a):
        while stack and array_a[stack[-1]] < num_a:
            array[stack.pop()] = num_a
        stack.append(i)
    print(*array)


if __name__ == "__main__":
    main()
