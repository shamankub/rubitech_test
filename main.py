import asyncio
import os

from task_1 import get_repository_names
from task_2 import create_ordered_dict
from task_3 import mutate_list
from task_4 import request_data
from task_5 import TextMethods

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

keys = ["g", 15, ("a", "k"), "c", ["b", "c"], "n"]
values = [1, 2, 3, 4]

my_list = ["1.73", 8, "def", 4, "ghi"]

url = "http://httpbin.org/delay/3"

text = "После настройки VM мы можем перейти к следующим шагам в создании кластера Kubernetes с использованием \"cri-o\" \
    в качестве контейнерного рантайма. Во-первых, нам необходимо внести несколько необходимых изменений, чтобы пройти \
    проверки при инициализации 'kubeadm init'. Об этих пунктах чуть ниже. В качестве первого шага мы должны следовать \
    главной рекомендации при работе с программным обеспечением — проверка на наличие обновлений и установка последних пакетов:"
my_text_object = TextMethods(text)


def clear_console():
    # Очистка окна терминала
    current_os = os.name

    if current_os == "posix":
        os.system("clear")
    elif current_os == "nt":
        os.system("cls")


if __name__ == "__main__":
    # clear_console()
    print("\nЗадание A:\n", get_repository_names(links))
    print("\nЗадание B:\n", create_ordered_dict(keys, values))
    print("\nЗадание C:\n", mutate_list(my_list))
    print("\nЗадание D:")
    asyncio.run(request_data(url))
    print("\nЗадание E, F:")
    print(my_text_object.find_longest_word())
    print(my_text_object.find_most_common_word())
    print(my_text_object.count_special_characters())
    print(my_text_object.find_palindromes())
