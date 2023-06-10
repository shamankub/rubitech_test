# Написать класс, принимающий на вход текст. Один метод класса должен выводить в консоль
# самое длинное слово в тексте. Второй метод - самое часто встречающееся слово. Третий метод
# выводит количество спецсимволов в тексте (точки, запятые и так далее). Четвертый метод выводит
# все палиндромы через запятую.

# Написать декоратор к предыдущему классу, который будет выводить в консоль время
# выполнения каждого метода. Результат выполнения задания должен быть оформлен в виде файла с кодом.

import time
from collections import Counter
from dataclasses import dataclass

from settings import TEXT


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"\nВремя выполнения '{func.__name__}' {elapsed_time:.6f} секунд")

        return result

    return wrapper


@dataclass
class TextMethods:
    text: str

    def _extract_words_from_text(self) -> list[str]:
        words = self.text.lower().split()
        extracted_words = [word.strip(".,!?;:—'\"") for word in words if word != "—"]
        return extracted_words

    @timer
    def find_longest_word(self) -> str:
        extracted_words = self._extract_words_from_text()
        longest_word = max(extracted_words, key=len)
        return f"Самое длинное слово в тексте: {longest_word}"

    @timer
    def find_most_common_word(self) -> str:
        extracted_words = self._extract_words_from_text()
        word_counts = Counter(extracted_words)
        most_common_word = max(word_counts, key=word_counts.get)
        return f"Самое часто встречающееся слово: {most_common_word}"

    @timer
    def count_special_characters(self) -> str:
        # Дефисы считал, как часть слова. Тире - как спецсимвол.
        special_chars = {".", ",", "!", "?", ";", ":", "—", "'", '"'}
        count = 0
        for char in self.text:
            if char in special_chars:
                count += 1
        return f"Количество спецсимволов в тексте: {count}"

    @timer
    def find_palindromes(self) -> str:
        extracted_words = self._extract_words_from_text()
        palindromes = {word for word in extracted_words if word == word[::-1]}
        palindromes_str = ", ".join(palindromes)
        return f"Палиндромы: {palindromes_str}"


if __name__ == "__main__":
    my_text_object = TextMethods(TEXT)
    print(my_text_object.find_longest_word())
    print(my_text_object.find_most_common_word())
    print(my_text_object.count_special_characters())
    print(my_text_object.find_palindromes())
