import os
import sys

import pytest

root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from task_3 import mutate_list


def test_mutate_list_with_strings():
    lst = ["123", "9", "ghi"]
    expected_output = ["abc_123_cba", "abc_9_cba", "abc_ghi_cba"]
    assert mutate_list(lst) == expected_output


def test_mutate_list_with_integers():
    lst = [1, 2, 3]
    expected_output = [1, 4, 9]
    assert mutate_list(lst) == expected_output


def test_mutate_list_with_float():
    lst = [1.2, 3, 4.1]
    expected_output = "Элемент списка может быть только типа <str> или <int>"
    assert mutate_list(lst) == expected_output


def test_mutate_list_with_boolean():
    lst = [True, False]
    expected_output = "Элемент списка может быть только типа <str> или <int>"
    assert mutate_list(lst) == expected_output


def test_mutate_list_with_none():
    lst = [None, "abc", 2]
    expected_output = "Элемент списка может быть только типа <str> или <int>"
    assert mutate_list(lst) == expected_output


def test_mutate_list_with_mixed_types():
    lst = ["1.73", 8, "def", 4, "ghi"]
    expected_output = ["abc_1.73_cba", 64, "abc_def_cba", 16, "abc_ghi_cba"]
    assert mutate_list(lst) == expected_output


def test_mutate_list_with_empty_list():
    lst = []
    expected_output = []
    assert mutate_list(lst) == expected_output


def test_mutate_list_with_single_element():
    lst = [5]
    expected_output = [25]
    assert mutate_list(lst) == expected_output


if __name__ == "__main__":
    pytest.main()
