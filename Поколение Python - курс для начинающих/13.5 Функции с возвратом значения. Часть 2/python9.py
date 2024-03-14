"""Functions."""


def convert_to_python_case(text: str) -> str:
    """Convert to snake case."""
    up_ind = [0] + [i for i, c in enumerate(text) if c.isupper()] + [len(text)]
    text = text.lower()
    return "_".join(text[i:j] for i, j in zip(up_ind, up_ind[1:]) if i != j)


def main():
    """My function."""
    txt = input()
    print(convert_to_python_case(txt))


if __name__ == "__main__":
    main()
