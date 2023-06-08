import os
import sys

import pytest
from httpx import Response

root_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_folder)

from task_4 import make_request, request_data


@pytest.mark.asyncio
async def test_make_request():
    url = "http://ya.ru"
    response = await make_request(url)
    assert isinstance(response, Response)
    assert response.status_code == 301


@pytest.mark.asyncio
async def test_request_data():
    url = "http://httpbin.org/delay/3"
    num_requests = 10
    await request_data(url, num_requests)


@pytest.mark.asyncio
async def test_request_data_with_invalid_url():
    url = "http://invalid-url"
    with pytest.raises(Exception):
        await request_data(url)


if __name__ == "__main__":
    pytest.main()
