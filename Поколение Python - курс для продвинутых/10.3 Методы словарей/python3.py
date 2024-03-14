"""Dictionaries."""


def main() -> dict[str, int]:
    """My function."""
    text = "".join(("footballcyberpunkextraterritorialityconversationalist",
                    "blockophthalmoscopicinterdependencemamauserfff"))
    res = {}
    for alpha in text:
        res[alpha] = res.get(alpha, 0) + 1
    return res


if __name__ == "__main__":
    result = main()
    print(result)
