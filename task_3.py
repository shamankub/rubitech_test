# Реализовать функцию с помощью методов map и lambda. Функция принимает список элементов
# (состоящий из строк и цифр), возвращает новый список, с условием - если элемент списка был
# строкой, в начало строки нужно добавить текст "abc_", в конец строки - "_cba". Если элемент был int -
# то его значение нужно возвести в квадрат. Результат вывести в консоль.

from typing import Union

my_list = ["1.73", 8, "def", 4, "ghi"]


def mutate_list(lst: list) -> Union[str, list]:
    # Надеюсь, что в ТЗ ошибка и список содержит числа, а не цифры. Иначе нужно добавить условие в 20 строке: 0 <= x < 10
    mutated_list = [None]
    try:
        mutated_list = list(
            map(
                lambda x: f"abc_{x}_cba"
                if isinstance(x, str)
                else x**2
                if isinstance(x, int) and not isinstance(x, bool)
                else None,
                lst,
            )
        )
        return mutated_list
    except TypeError:
        return "Элемент списка может быть только типа <str> или <int>"
    finally:
        if None in mutated_list:
            return "Элемент списка может быть только типа <str> или <int>"


if __name__ == "__main__":
    print(mutate_list(my_list))
