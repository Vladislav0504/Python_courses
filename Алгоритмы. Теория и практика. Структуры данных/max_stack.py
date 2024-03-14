"""Basic data structures."""
from sys import stdin, stdout


def main():
    """My function."""
    _, stack = input(), [(-1, -1)]
    for line in stdin:
        operation, *num = line.split()
        maximum = stack[-1][1]
        if operation == "push":
            k = int(num[0])
            stack.append((k, max(maximum, k)))
        elif operation == "pop":
            stack.pop()
        else:
            stdout.write(f"{maximum}\n")


if __name__ == "__main__":
    main()
