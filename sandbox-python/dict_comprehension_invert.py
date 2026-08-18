#!/usr/bin/env python3
"""
Task: Demonstrate dictionary comprehension and inversion with pprint.
Run: python3 dict_comprehension_invert.py
Status: Done
"""

from pprint import pprint
from typing import Dict, Any


def create_mapped_dict(n: int) -> Dict[int, str]:
    """
    Создаёт словарь {i: str(i*2)} для i от 0 до n-1.

    Args:
        n: Количество элементов.

    Returns:
        Словарь с целочисленными ключами и строковыми значениями.
    """
    return {i: str(i * 2) for i in range(n)}


def invert_dict_safe(original: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Меняет местами ключи и значения словаря.

    Args:
        original: Исходный словарь.

    Returns:
        Новый словарь, где ключи — старые значения, а значения — старые ключи.

    Warning:
        Если в исходном словаре есть повторяющиеся значения, они будут перезаписаны
        (последнее встреченное значение станет ключом).
    """
    return {value: key for key, value in original.items()}


if __name__ == "__main__":
    # Генерируем словарь
    n = 10
    original_dict = create_mapped_dict(n)

    print("Исходный словарь (сгенерированный):")
    pprint(original_dict)

    # Инвертируем
    inverted_dict = invert_dict_safe(original_dict)

    print("\nИнвертированный словарь (ключи и значения поменяны местами):")
    pprint(inverted_dict)
