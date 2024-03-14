"""Dictionaries."""


def main():
    """My function."""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    morse = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
             ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",
             "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----",
             ".----", "..---", "...--", "....-", ".....", "-....", "--...",
             "---..", "----.")
    data = dict(zip(letters, map(lambda x: f"{x} ", morse)))
    message = input()
    print(*(data.get(alpha, "") for alpha in message.upper()), sep="")


if __name__ == "__main__":
    main()
