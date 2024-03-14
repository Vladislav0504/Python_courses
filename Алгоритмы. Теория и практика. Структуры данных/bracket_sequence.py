"""Basic data structures."""


def main():
    """My function."""
    stack, bracket = [], {")": "(", "]": "[", "}": "{"}
    for i, char in enumerate(input(), 1):
        if char in "([{":
            stack.append((char, i))
        if char in ")]}" and not (stack and bracket[char] == stack.pop()[0]):
            stack.append((char, i))
            break
    print(stack.pop()[1] if stack else "Success")


if __name__ == "__main__":
    main()
