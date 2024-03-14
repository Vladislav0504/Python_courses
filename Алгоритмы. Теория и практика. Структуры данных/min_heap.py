"""Priority queue."""


def build_heap(array: list[int], swaps: list[(int, int)]) -> None:
    """Build heap."""
    for i in range(len(array) - 1 >> 1, -1, -1):
        sift_down(array, i, swaps)


def sift_down(array: list[int], i: int, swaps: list[(int, int)]) -> None:
    """Sift down index i."""
    j = (i << 1) + 1
    while j < len(array):
        k = j + 1
        if k < len(array) and array[j] > array[k]:
            j = k
        if array[i] <= array[j]:
            break
        array[i], array[j] = array[j], array[i]
        swaps.append((i, j))
        i = j
        j = (i << 1) + 1


def main():
    """My function."""
    _, array_a, swaps = input(), list(map(int, input().split())), []
    build_heap(array_a, swaps)
    print(len(swaps))
    print(*(f"{i} {j}" for i, j in swaps), sep="\n")


if __name__ == "__main__":
    main()
