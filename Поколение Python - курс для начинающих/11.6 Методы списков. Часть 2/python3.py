"""Lists."""


def main():
    """My function."""
    text, articles = input(), ("a", "an", "the")
    words = text.lower().split()
    total = sum(words.count(article) for article in articles)
    print(f"Общее количество артиклей: {total}")


if __name__ == "__main__":
    main()
