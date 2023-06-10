import asyncio
import os

from settings import KEYS, LINKS, MY_LIST, TEXT, URL, VALUES
from task_1 import get_repository_names
from task_2 import create_ordered_dict
from task_3 import mutate_list
from task_4 import request_data
from task_5 import TextMethods


my_text_object = TextMethods(TEXT)


def clear_console():
    # Очистка окна терминала
    current_os = os.name

    if current_os == "posix":
        os.system("clear")
    elif current_os == "nt":
        os.system("cls")


if __name__ == "__main__":
    # clear_console()
    print("\nЗадание A:\n", get_repository_names(LINKS))
    print("\nЗадание B:\n", create_ordered_dict(KEYS, VALUES))
    print("\nЗадание C:\n", mutate_list(MY_LIST))
    print("\nЗадание D:")
    asyncio.run(request_data(URL))
    print("\nЗадание E, F:")
    print(my_text_object.find_longest_word())
    print(my_text_object.find_most_common_word())
    print(my_text_object.count_special_characters())
    print(my_text_object.find_palindromes())
