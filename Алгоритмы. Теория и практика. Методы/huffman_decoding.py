"""Greedy algorithms."""
from sys import stdin


def main():
    """My function."""
    dictionary_length, _ = map(int, input().split())
    init = -1
    tree, index = [[init, init, ""]], 0
    for _ in range(dictionary_length):
        char, code = stdin.readline().strip().split(": ")
        for num in map(int, code):
            node = tree[index]
            if node[num] == -1:
                index = len(tree)
                node[num] = index
                tree.append([init, init, ""])
            else:
                index = node[num]
        index, tree[-1][2] = 0, char
    encoded_string, decode = input(), []
    for code_0 in encoded_string:
        index = tree[index][int(code_0)]
        char = tree[index][2]
        if char:
            decode.append(char)
            index = 0
    print("".join(decode))


if __name__ == "__main__":
    main()
