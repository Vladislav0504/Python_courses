"""Contest."""


def main():
    """My function."""
    num_n, num_k = list(input()), int(input())
    sequence, last = [0] * 10, 0
    for i, num in enumerate(map(int, num_n + ["-1"])):
        for j in range(last, num, -1):
            minimum = min(sequence[j], num_k)
            sequence[j] -= minimum
            num_k -= minimum
        if num_k:
            last = num
            sequence[last] += 1
        else:
            sequence = [str(k) * count for k, count in enumerate(sequence)]
            print(int("".join(sequence + num_n[i:])))
            break


if __name__ == "__main__":
    main()
