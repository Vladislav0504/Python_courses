"""Array. Stack. Queue."""


def main():
    """My function."""
    stack = []
    for char in input().split():
        if char == "+":
            stack.append(stack.pop() + stack.pop())
        elif char == "-":
            stack.append(-stack.pop() + stack.pop())
        elif char == "*":
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(char))
    print(stack.pop())


if __name__ == "__main__":
    main()
