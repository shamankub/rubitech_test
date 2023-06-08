# Функция принимает в качестве аргумента набор ссылок. Ссылки имеют формат ссылок на
# проекты на гитхабе (например: https://github.com/miguelgrinberg/Flask-SocketIO,
# https://github.com/miguelgrinberg/Flask-SocketIO.git). Функция должна обработать полученные ссылки
# и вывести в консоль названия самих гит-проектов. Стоит рассмотреть защиту от ссылок "вне формата".

import re
from urllib.parse import urlparse

links = [
    "https://github.com/miguelgrinberg/Flask-SocketIO.git",
    "https://github.com/miguelgrinberg/Flask-SocketIO",
    "https://github.com/someuser/someproject",
    "https://github.com/someuser/repository.name.gi.git",
    "https://github.com/someuser/repository.name.git.git",
    "https://github.com/someuser/repository/name.git",
    "http://google.com",
    "non-valid link",
    12345,
]


def get_repository_names(links: list) -> str:
    res = []
    if not links:
        res.append("Передан пустой список.")
    for link in links:
        try:
            if not re.match(r"^https?://github.com/.+/?$", link):
                res.append(f"Неправильный формат ссылки: {link}")
            else:
                parsed_url = urlparse(link)
                repository_name = parsed_url.path.strip("/")
                if repository_name.count("/") > 1:
                    res.append((f"Некорректное название репозитория: {link}"))
                elif repository_name.endswith(".git"):
                    repository_name = repository_name[:-4]
                    if repository_name.endswith(".git"):
                        res.append((f"Некорректное название репозитория: {link}"))
                    else:
                        res.append(repository_name)
                else:
                    res.append(repository_name)
        except TypeError:
            res.append((f"Ссылка должна быть строкой: {link}"))

    return "\n".join(res)


if __name__ == "__main__":
    print(get_repository_names(links))
