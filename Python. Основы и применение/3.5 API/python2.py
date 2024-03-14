"""API."""
from requests import post, get


def main():
    """My function."""
    client_id = "1eb649744aaabdedeed8"
    client_secret = "886dc091519ebc328f6b9a27f5ccceee"

    # инициируем запрос на получение токена
    response = post("https://api.artsy.net/api/tokens/xapp_token",
                    timeout=10,
                    data={"client_id": client_id,
                          "client_secret": client_secret})

    # создаем заголовок, содержащий наш токен
    headers = {"X-Xapp-Token": response.json()["token"]}
    lst = []
    with open("dataset_24476_4.txt", "r", encoding="utf8") as file:
        for line in file:
            url = "https://api.artsy.net/api/artists/" + line.strip()
            # инициируем запрос с заголовком
            my_dict = get(url, timeout=10, headers=headers).json()
            lst.append((int(my_dict["birthday"]), my_dict["sortable_name"]))
    print(*(name for _, name in sorted(lst)), sep="\n")


if __name__ == "__main__":
    main()
