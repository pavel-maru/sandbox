#!/usr/bin/env python3
"""
Task: Find all indices of a given character in a string using two approaches.
Run: python3 find_char_positions.py
Status: Done
"""

from typing import List, Optional


def find_indices_with_index(text: str, char: str) -> List[int]:
    """
    Находит все позиции символа в строке, используя метод str.index() в цикле.

    Args:
        text: Исходная строка.
        char: Искомый символ (строка длиной 1).

    Returns:
        Список индексов, где встречается char.

    Raises:
        ValueError: если char не является строкой длины 1.

    Note:
        Метод index() выбрасывает ValueError, если символ не найден,
        поэтому используется try/except для завершения цикла.
    """
    if len(char) != 1:
        raise ValueError("char must be a single character")

    indices = []
    pos = 0
    while True:
        try:
            pos = text.index(char, pos, len(text))
            indices.append(pos)
            pos += 1  # продолжить поиск со следующего символа
        except ValueError:
            break
    return indices


def find_indices_with_enumerate(text: str, char: str) -> List[int]:
    """
    Находит все позиции символа в строке, используя enumerate() и сравнение.

    Args:
        text: Исходная строка.
        char: Искомый символ (строка длиной 1).

    Returns:
        Список индексов, где встречается char.

    Raises:
        ValueError: если char не является строкой длины 1.
    """
    if len(char) != 1:
        raise ValueError("char must be a single character")

    return [i for i, ch in enumerate(text) if ch == char]


if __name__ == "__main__":
    test_text = "alan wake"
    search_char = 'a'

    print(f"Исходная строка: '{test_text}'")
    print(f"Ищем символ: '{search_char}'\n")

    indices1 = find_indices_with_index(test_text, search_char)
    print(f"Метод index():     {indices1}")

    indices2 = find_indices_with_enumerate(test_text, search_char)
    print(f"Метод enumerate(): {indices2}")

    # Демонстрация работы с символом, которого нет
    missing_char = 'z'
    print(f"\nПоиск символа '{missing_char}':")
    print(f"  index():     {find_indices_with_index(test_text, missing_char)}")
    print(f"  enumerate(): {find_indices_with_enumerate(test_text, missing_char)}")

    # Обработка ошибки (необязательно, просто для проверки)
    try:
        find_indices_with_index(test_text, "ab")
    except ValueError as e:
        print(f"\nОшибка при неверном символе: {e}")
