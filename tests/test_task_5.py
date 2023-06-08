import os
import sys

import pytest

root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from task_5 import TextMethods


@pytest.fixture
def my_text_object():
    text = "После настройки VM мы можем перейти к следующим шагам в создании кластера Kubernetes с использованием \"cri-o\" \
    в качестве контейнерного рантайма. Во-первых, нам необходимо внести несколько необходимых изменений, чтобы пройти \
    проверки при инициализации 'kubeadm init'. Об этих пунктах чуть ниже. В качестве первого шага мы должны следовать \
    главной рекомендации при работе с программным обеспечением — проверка на наличие обновлений и установка последних пакетов:"
    return TextMethods(text)


def test_find_longest_word(my_text_object):
    result = my_text_object.find_longest_word()
    expected_output = "Самое длинное слово в тексте: использованием"
    assert isinstance(result, str)
    assert result == expected_output


def test_find_most_common_word(my_text_object):
    result = my_text_object.find_most_common_word()
    expected_output = "Самое часто встречающееся слово: в"
    assert isinstance(result, str)
    assert result == expected_output


def test_count_special_characters(my_text_object):
    result = my_text_object.count_special_characters()
    expected_output = "Количество спецсимволов в тексте: 11"
    assert isinstance(result, str)
    assert result == expected_output


def test_find_palindromes(my_text_object):
    result = my_text_object.find_palindromes()
    assert isinstance(result, str)
    assert result.startswith("Палиндромы: ")
    assert "в" and "и" and "к" and "с" in result.split(":")[1]


if __name__ == "__main__":
    pytest.main()
