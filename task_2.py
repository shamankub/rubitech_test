# Реализовать функцию, принимающую два списка и возвращающую словарь (ключ из первого
# списка, значение из второго), упорядоченный по ключам. Результат вывести в консоль. Длина
# первого списка не должна быть равна длине второго. Результат вывести в консоль.

from typing import Union

keys = ["g", 15, ("a", "k"), "c", ["b", "c"], "n"]
values = [1, 2, 3, 4]


def create_ordered_dict(keys: list, values: list) -> Union[str, dict]:
    try:
        list(map(hash, keys[: len(values)]))
    except TypeError:
        return "Ключом словаря может быть только хэшируемый объект"

    if keys == values == []:
        return "Оба списка пустые"
    elif len(keys) == len(values):
        return "Длина первого списка не должна быть равна длине второго"

    # Чтобы отсортировать кортежи, числа и строки по алфавиту, приводим ключи к типу <str>
    ordered_dict = {str(el[0]): el[1] for el in zip(keys, values)}
    return dict(sorted(ordered_dict.items()))


if __name__ == "__main__":
    print(create_ordered_dict(keys, values))
