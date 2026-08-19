#!/usr/bin/env python3
"""
Task: Convert a string into a list of alphabet positions (A=1, B=2, ...).
Run: python3 alphabet_positions.py
Status: Done
"""

from typing import List, Optional

# Русский алфавит (включая 'ё')
RUSSIAN_ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# Английский алфавит
ENGLISH_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def get_positions(text: str, language: str = 'ru') -> List[int]:
    """
    Возвращает список порядковых номеров букв в строке.
    Регистр игнорируется.

    Args:
        text: Исходная строка (только буквы).
        language: 'ru' для русского алфавита, 'en' для английского.

    Returns:
        Список чисел (1-индексация) для каждой буквы.

    Raises:
        ValueError: если в строке есть символ, не являющийся буквой выбранного алфавита.
    """
    if language == 'ru':
        alphabet = RUSSIAN_ALPHABET
    elif language == 'en':
        alphabet = ENGLISH_ALPHABET
    else:
        raise ValueError("language must be 'ru' or 'en'")

    # Создаём словарь для быстрого поиска
    char_to_pos = {char: idx + 1 for idx, char in enumerate(alphabet)}

    positions = []
    for sym in text.lower():
        if sym in char_to_pos:
            positions.append(char_to_pos[sym])
        else:
            raise ValueError(f"Символ '{sym}' не найден в {language} алфавите")
    return positions


def positions_to_number(positions: List[int]) -> int:
    """
    Преобразует список позиций в одно число (конкатенацией цифр).
    Внимание: это работает только если все позиции однозначные (1-9).
    Для многозначных чисел результат будет неоднозначным.

    Args:
        positions: Список чисел.

    Returns:
        Число, образованное последовательной записью цифр.

    Examples:
        >>> positions_to_number([1, 2, 3])
        123
    """
    return int(''.join(str(p) for p in positions))


def main() -> None:
    """Демонстрация работы."""
    test_strings = ['альфа', 'мед', 'abc', 'Hello']
    for s in test_strings:
        try:
            # Русский алфавит
            if any('а' <= c <= 'я' or c == 'ё' for c in s.lower()):
                lang = 'ru'
            else:
                lang = 'en'
            positions = get_positions(s, lang)
            print(f"Строка: '{s}' -> позиции: {positions}")
            # Если все позиции однозначные, покажем конкатенацию
            if all(1 <= p <= 9 for p in positions):
                num = positions_to_number(positions)
                print(f"  → как число: {num}")
        except ValueError as e:
            print(f"Ошибка для '{s}': {e}")


if __name__ == "__main__":
    main()
