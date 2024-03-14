"""Random."""
from random import randrange


def generate_index() -> str:
    """Generate index."""
    min_letter, max_letter, max_num = 65, 91, 100
    lst = [chr(randrange(min_letter, max_letter)) for _ in range(2)]
    lst.append(str(randrange(max_num)))
    lst.append("_")
    lst.append(str(randrange(max_num)))
    lst.extend([chr(randrange(min_letter, max_letter)) for _ in range(2)])
    return "".join(lst)


def main():
    """My function."""
    print(generate_index())


if __name__ == "__main__":
    main()
