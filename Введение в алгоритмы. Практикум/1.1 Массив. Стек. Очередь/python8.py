"""Array. Stack. Queue."""


def main():
    """My function."""
    array_h, k = list(map(int, input().split())), 0
    stack = []
    for height in array_h:
        while stack and height < stack[-1]:
            k += 1
            stack.pop()
        if not stack or height > stack[-1]:
            stack.append(height)
    print(k + len(stack) - (stack and stack[0] == 0))


if __name__ == "__main__":
    main()
