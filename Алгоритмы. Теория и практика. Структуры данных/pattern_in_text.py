"""Hash tables."""


def my_hash(string: str, prime: int, num_x: int) -> int:
    """Hash function."""
    k = ord(string[-1])
    for char in string[-2::-1]:
        k = (k * num_x + ord(char)) % prime
    return k


def main():
    """My function."""
    pattern, text, indexes = input(), input(), []
    prime, num_x, len_p = 1000000007, 263, len(pattern)
    x_p_1 = pow(num_x, len_p - 1, prime)
    h_pattern = my_hash(pattern, prime, num_x)
    h_text = my_hash(text[-len_p:], prime, num_x)
    for i in range(len(text) - len_p, -1, -1):
        if h_text == h_pattern and text[i:i + len_p] == pattern:
            indexes.append(i)
        t_i_p, t_i = ord(text[i + len_p - 1]), ord(text[i - 1])
        h_text = ((h_text - t_i_p * x_p_1) * num_x + t_i) % prime
    print(*indexes[::-1])


if __name__ == "__main__":
    main()
