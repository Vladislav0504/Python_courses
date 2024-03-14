"""Project."""


def caesar(text: str, mod: int) -> str:
    """Caesar's cipher."""
    result, step, init_orders = [], 0, [ord("A"), ord("a")]
    for i, char in enumerate(text):
        if step == 0:
            while i + step < len(text) and text[i + step].isalpha():
                step += 1
        if char.isalpha():
            order = ord(char) - init_orders[char.islower()] + step
            char = chr(order % mod + init_orders[char.islower()])
        else:
            step = 0
        result.append(char)
    return "".join(result)


def main():
    """My function."""
    text, mod = input(), 26
    print(caesar(text, mod))


if __name__ == "__main__":
    main()
