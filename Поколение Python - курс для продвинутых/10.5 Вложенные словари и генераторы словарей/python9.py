"""Dictionaries."""


def main() -> dict[str, (int, int)]:
    """My function."""
    students = {"Timur": (170, 75), "Ruslan": (180, 105), "Soltan": (192, 68),
                "Roman": (175, 70), "Madlen": (160, 50), "Stefani": (165, 70),
                "Tom": (190, 90), "Jerry": (180, 87), "Anna": (172, 67),
                "Scott": (168, 78), "John": (186, 79), "Alex": (195, 120),
                "Max": (200, 110), "Barak": (180, 89), "Donald": (170, 80),
                "Rustam": (186, 100), "Alice": (159, 59), "Rita": (170, 80),
                "Mary": (175, 69), "Jane": (190, 80)}
    height_limit, weight_limit = 167, 75
    return {name: (height, weight)
            for name, (height, weight) in students.items()
            if height > height_limit and weight < weight_limit}


if __name__ == "__main__":
    result = main()
    print(result)
