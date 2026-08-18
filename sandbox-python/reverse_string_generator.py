#!/usr/bin/env python3
"""
Task: Reverse a string using a recursive generator with yield/yield from.
Run: python3 reverse_string_generator.py
Status: Done
"""

from typing import Iterator


def reverse_string_gen(text: str) -> Iterator[str]:
    """
    Генератор, рекурсивно возвращающий символы строки в обратном порядке.

    Args:
        text: Исходная строка.

    Yields:
        Символы строки, начиная с последнего.

    Note:
        Рекурсивный подход ограничен глубиной рекурсии (по умолчанию ~1000),
        поэтому для очень длинных строк (> 1000 символов) лучше использовать
        срезы или итеративный подход.

    Example:
        >>> list(reverse_string_gen("abc"))
        ['c', 'b', 'a']
        >>> ''.join(reverse_string_gen("stressed"))
        'desserts'
    """
    if text:  # если строка не пуста
        yield text[-1]                # возвращаем последний символ
        yield from reverse_string_gen(text[:-1])  # рекурсивно обрабатываем остаток


def reverse_string_iterative(text: str) -> str:
    """
    Итеративный способ разворота строки (без рекурсии) — более эффективный и безопасный.

    Args:
        text: Исходная строка.

    Returns:
        Перевёрнутая строка.
    """
    return text[::-1]


if __name__ == "__main__":
    original = "stressed"
    reversed_gen = ''.join(reverse_string_gen(original))
    reversed_slice = reverse_string_iterative(original)

    print(f"Исходная строка: {original}")
    print(f"Разворот (генератор): {reversed_gen}")
    print(f"Разворот (срез):     {reversed_slice}")

    # Проверяем, что результат совпадает
    assert reversed_gen == reversed_slice == original[::-1]
    print("✅ Оба метода дают одинаковый результат.")

    # Демонстрация для пустой строки
    empty = ""
    print(f"\nПустая строка: '{empty}' -> '{''.join(reverse_string_gen(empty))}'")
