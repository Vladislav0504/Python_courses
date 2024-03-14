"""Greedy algorithms."""


def pre_order(node: int, dictionary: dict[str, str],
              code: list[int], nodes: list[(int, int, str)]) -> None:
    """Pre-order."""
    if node >= 0:
        char = nodes[node][2]
        if char:
            dictionary[char] = "".join(str(num) for num in code)
            return
        for i in (0, 1):
            code.append(i)
            pre_order(nodes[node][i], dictionary, code, nodes)
            code.pop()


def main():
    """My function."""
    string = input()
    frequencies, dictionary = {}, {}
    for char_0 in string:
        frequencies[char_0] = frequencies.get(char_0, 0) + 1
    num_n = len(frequencies)
    nodes = list(zip([-1] * num_n, [-1] * num_n, frequencies))
    heap = [(frequency, i) for i, frequency in enumerate(frequencies.values())]
    for k in range(num_n, (num_n << 1) - 1):
        frequency_0, node_0 = heap.pop(heap.index(min(heap)))
        frequency_1, node_1 = heap.pop(heap.index(min(heap)))
        nodes.append((node_0, node_1, ""))
        new_frequency = frequency_0 + frequency_1
        heap.append((new_frequency, k))
    if heap:
        pre_order(heap[0][1], dictionary, [], nodes)
    if len(dictionary) == 1:
        dictionary[string[0]] = "0"
    result = "".join(dictionary[char_1] for char_1 in string)
    print(len(frequencies), len(result))
    print(*(f"{char}: {code}" for char, code in dictionary.items()), sep="\n")
    print(result)


if __name__ == "__main__":
    main()
