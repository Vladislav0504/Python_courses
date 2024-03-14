"""Array. Stack. Queue."""


def main():
    """My function."""
    brackets, stack = {")": "(", "]": "[", "}": "{"}, []
    string = input()
    for char in string:
        if char in brackets.values():
            stack.append(char)
        if char in brackets and not (stack and brackets[char] == stack.pop()):
            stack.append(char)
            break
    print("WRONG" if stack else "CORRECT")


if __name__ == "__main__":
    main()
