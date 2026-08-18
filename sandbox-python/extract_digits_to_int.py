#!/usr/bin/env python3
"""
Task: Extract integer from string by removing all non-digit characters.
Run: python3 extract_digits_to_int.py
Status: Done
"""

from typing import Optional

def extract_number_from_string(text: str) -> Optional[int]:
    """
    Извлекает целое число из строки, оставляя только цифры.

    Args:
        text: Исходная строка, например '1 000 000 Р'.

    Returns:
        Целое число или None, если в строке нет цифр.
    """
    digits = ''.join(ch for ch in text if ch.isdigit())
    if not digits:
        return None
    return int(digits)

if __name__ == "__main__":
    price_str = '1 000 000 Р'
    number = extract_number_from_string(price_str)
    print(f"Исходная строка: {price_str}")
    print(f"Извлечённое число: {number}")
