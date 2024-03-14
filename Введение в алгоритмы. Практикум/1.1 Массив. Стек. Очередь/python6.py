"""Array. Stack. Queue."""


def main():
    """My function."""
    stack, result = [], 0
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    for fish, direction in zip(list_a, list_b):
        if direction == 0:
            while stack and fish > stack[-1]:
                stack.pop()
            if not stack:
                result += 1
        else:
            stack.append(fish)
    print(result + len(stack))


if __name__ == "__main__":
    main()
