"""Exam."""


def main():
    """My function."""
    translation = {"G": "C", "C": "G", "T": "A", "A": "U"}
    dna = input()
    rna = "".join(translation[char] for char in dna)
    print(rna)


if __name__ == "__main__":
    main()
