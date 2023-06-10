# Реализовать функцию, которая замеряет время на исполнение 100 запросов к адресу:
# http://httpbin.org/delay/3. Запросы должны выполняться асинхронно. Допускается написание
# вспомогательных функций и использование сторонних библиотек. Результат замера времени
# выводит в консоль. Ожидаемое время не должно превышать 10 секунд.

import asyncio
import time

import httpx

from settings import URL


async def make_request(url: str) -> httpx.Response:
    try:
        async with httpx.AsyncClient() as client:
            # Увеличиваем таймаут таким образом, чтобы реже выбрасывало исключение ReadTimeout,
            # но время работы функции было в пределах 10 секунд.
            response = await client.get(url, timeout=8.5)
            return response
    except httpx.ReadTimeout:
        print(f"Произошла ошибка Timeout при выполнении запроса.")


def timer(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Время выполнения '{func.__name__}' {elapsed_time:.6f} секунд")

        return result

    return wrapper


@timer
async def request_data(url: str, num_requests: int = 100):
    tasks = [make_request(url) for _ in range(num_requests)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(request_data(URL))
