#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль для подсчёта количества и позиций заданной буквы в строке.

Функция count_letter возвращает количество вхождений и список позиций (1-индексация).
Пример использования:
    count, positions = count_letter("искуство", "с")
    print(count)  # 2
    print(positions)  # [3, 6] (в слове "искуство" буква "с" на позициях 3 и 6)
"""

from typing import Tuple, List


def count_letter(text: str, letter: str) -> Tuple[int, List[int]]:
    """
    Подсчитывает количество вхождений буквы letter в строке text и возвращает
    список позиций (нумерация с 1).

    Args:
        text: Исходная строка.
        letter: Искомая буква (строка длиной 1).

    Returns:
        Кортеж (количество, список позиций). Если letter не найдена, список пуст.

    Raises:
        ValueError: если letter не является строкой длиной 1.
    """
    if len(letter) != 1:
        raise ValueError("letter must be a single character")
    count = text.count(letter)
    positions = [i + 1 for i, char in enumerate(text) if char == letter]
    return count, positions


def main() -> None:
    """Демонстрация работы функции на примере."""
    word = "искусство"
    letter = "с"
    try:
        count, positions = count_letter(word, letter)
        print(f"Слово: '{word}'")
        print(f"Ищем букву: '{letter}'")
        print(f"Количество вхождений: {count}")
        if positions:
            print(f"Позиции (начиная с 1): {positions}")
        else:
            print("Буква не найдена.")
    except ValueError as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
