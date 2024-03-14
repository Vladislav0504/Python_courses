"""Namespaces."""


def main():
    """My function."""
    num_n = int(input())
    space = {"global": ("None", set()), "None": ("None", set())}
    for _ in range(num_n):
        instruction, namespace, name = input().split()
        if instruction == "create":
            space[namespace] = (name, set())
        elif instruction == "add":
            space[namespace][1].add(name)
        else:
            space["None"][1].add(name)
            while name not in space[namespace][1]:
                namespace = space[namespace][0]
            print(namespace)


if __name__ == "__main__":
    main()
