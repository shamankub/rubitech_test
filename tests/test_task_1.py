import os
import sys

import pytest

root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from task_1 import get_repository_names


def test_empty_list():
    links = []
    expected_output = "Передан пустой список."
    assert get_repository_names(links) == expected_output


def test_invalid_link_format():
    links = [
        "https://github.com/someuser/repository.name.git.git",
        "https://github.com/someuser/repository/name.git",
        "http://google.com",
        "non-valid link",
        12345,
    ]
    expected_output = "Некорректное название репозитория: https://github.com/someuser/repository.name.git.git\nНекорректное название репозитория: https://github.com/someuser/repository/name.git\nНеправильный формат ссылки: http://google.com\nНеправильный формат ссылки: non-valid link\nСсылка должна быть строкой: 12345"
    assert get_repository_names(links) == expected_output


def test_valid_links():
    links = [
        "https://github.com/miguelgrinberg/Flask-SocketIO.git",
        "https://github.com/miguelgrinberg/Flask-SocketIO",
        "https://github.com/someuser/someproject",
        "https://github.com/someuser/repository.name.gi.git",
    ]
    expected_output = "miguelgrinberg/Flask-SocketIO\nmiguelgrinberg/Flask-SocketIO\nsomeuser/someproject\nsomeuser/repository.name.gi"
    assert get_repository_names(links) == expected_output


if __name__ == "__main__":
    pytest.main()
