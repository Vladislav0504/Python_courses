"""Exam."""


def main():
    """My function."""
    emails = {"nosu.edu": ["timyr", "joseph", "svetlana.gaeva",
                           "larisa.mamuk"],
              "gmail.com": ["ruslan.chaika", "rustam.mini", "stepik-best"],
              "msu.edu": ["apple.fruit", "beegeek", "beegeek.school"],
              "yandex.ru": ["surface", "google"],
              "hse.edu": ["tomas-henders", "cream.soda", "zivert"],
              "mail.ru": ["angel.down", "joanne", "the.fame.moster"]}
    res = [f"{name}@{dom}" for dom, lst in emails.items() for name in lst]
    print(*sorted(res), sep="\n")


if __name__ == "__main__":
    main()
