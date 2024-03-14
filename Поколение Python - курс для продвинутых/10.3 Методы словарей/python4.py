"""Dictionaries."""


def main():
    """My function."""
    string = """orange strawberry barley gooseberry apple apricot barley
    currant orange melon pomegranate banana banana orange barley apricot plum
    grapefruit banana quince strawberry barley grapefruit banana grapes melon
    strawberry apricot currant currant gooseberry raspberry apricot currant
    orange lime quince grapefruit barley banana melon pomegranate barley banana
    orange barley apricot plum banana quince lime grapefruit strawberry
    gooseberry apple barley apricot currant orange melon pomegranate banana
    banana orange apricot barley plum banana grapefruit banana quince currant
    orange melon pomegranate barley plum banana quince barley lime grapefruit
    pomegranate barley"""
    dictionary = {}
    for word in string.split():
        dictionary[word] = dictionary.get(word, 0) + 1
    key, _ = min(dictionary.items(), key=lambda pair: (-pair[1], pair[0]))
    print(key)


if __name__ == "__main__":
    main()
