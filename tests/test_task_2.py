import os
import sys

import pytest

root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from task_2 import create_ordered_dict


def test_create_ordered_dict_unhashable_key_in_dict():
    keys = [["b", "c"], "a", "d"]
    values = [1, 2, 3, 4, 5]
    result = create_ordered_dict(keys, values)
    expected_output = "Ключом словаря может быть только хэшируемый объект"
    assert isinstance(result, str)
    assert result == expected_output


def test_create_ordered_dict_unhashable_key_not_in_dict():
    keys = ["g", "j", "c", "a", ["b", "c"], "n"]
    values = [1, 2, 3, 4]
    result = create_ordered_dict(keys, values)
    expected_output = {'a': 4, 'c': 3, 'g': 1, 'j': 2}
    assert isinstance(result, dict)
    assert result == expected_output


def test_create_ordered_dict_with_tuple_in_key():
    keys = ["g", "j", ("a", "k"), "c", ["b", "c"], "n"]
    values = [1, 2, 3, 4]
    result = create_ordered_dict(keys, values)
    expected_output = {"('a', 'k')": 3, 'c': 4, 'g': 1, 'j': 2}
    assert isinstance(result, dict)
    assert result == expected_output


def test_create_ordered_dict_with_list_in_tuple_in_key():
    keys = ["g", "j", ("a", ["k"]), "c", ["b", "c"], "n"]
    values = [1, 2, 3, 4]
    result = create_ordered_dict(keys, values)
    expected_output = "Ключом словаря может быть только хэшируемый объект"
    assert isinstance(result, str)
    assert result == expected_output


def test_create_ordered_dict_with_integer_in_key():
    keys = ["g", 15, ("a", "k"), "c", ["b", "c"], "n"]
    values = [1, 2, 3, 4]
    result = create_ordered_dict(keys, values)
    expected_output = {"('a', 'k')": 3, '15': 2, 'c': 4, 'g': 1}
    assert isinstance(result, dict)
    assert result == expected_output


def test_create_ordered_dict_equal_lengths():
    keys = ["b", "c", "a"]
    values = [1, 2, 3]
    result = create_ordered_dict(keys, values)
    expected_output = "Длина первого списка не должна быть равна длине второго"
    assert isinstance(result, str)
    assert result == expected_output


def test_create_ordered_dict_different_lengths():
    keys = ["b", "c", "a", "d"]
    values = [1, 2, 3, 4, 5]
    result = create_ordered_dict(keys, values)
    expected_output = {"a": 3, "b": 1, "c": 2, "d": 4}
    assert isinstance(result, dict)
    assert result == expected_output


def test_create_ordered_dict_empty_lists():
    keys = []
    values = []
    result = create_ordered_dict(keys, values)
    expected_output = "Оба списка пустые"
    assert isinstance(result, str)
    assert result == expected_output


def test_create_ordered_dict_empty_values():
    keys = ["a", "b", "c"]
    values = []
    result = create_ordered_dict(keys, values)
    expected_output = {}
    assert isinstance(result, dict)
    assert result == expected_output


def test_create_ordered_dict_empty_keys():
    keys = []
    values = [1, 2, 3]
    result = create_ordered_dict(keys, values)
    expected_output = {}
    assert isinstance(result, dict)
    assert result == expected_output


if __name__ == "__main__":
    pytest.main()
