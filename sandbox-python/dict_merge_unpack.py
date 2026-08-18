#!/usr/bin/env python3
"""
Task: Merge two dictionaries using unpacking, and compare with other methods.
Run: python3 dict_merge_unpack.py
Status: Done
"""

import sys
from typing import Dict, Any


def merge_with_unpacking(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Объединяет два словаря через распаковку: {**dict1, **dict2}.

    Args:
        dict1: Первый словарь.
        dict2: Второй словарь.

    Returns:
        Новый словарь, содержащий все элементы из dict1 и dict2.
        При совпадении ключей значения из dict2 перезаписывают значения из dict1.
    """
    return {**dict1, **dict2}


def merge_with_update(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Объединяет словари, создавая копию первого и обновляя её элементами второго.
    Использует метод update().

    Args:
        dict1: Первый словарь.
        dict2: Второй словарь.

    Returns:
        Новый словарь — объединение dict1 и dict2.
    """
    result = dict1.copy()
    result.update(dict2)
    return result


if __name__ == "__main__":
    a = {1: 'a', 2: 'b'}
    b = {3: 'c', 4: 'd'}

    print("Исходные словари:")
    print(f"  a = {a}")
    print(f"  b = {b}\n")

    # Объединение распаковкой
    c_unpack = merge_with_unpacking(a, b)
    # Экранируем фигурные скобки в f-строке (удваиваем)
    print(f"1. Распаковка {{**a, **b}}:  {c_unpack}")

    # Объединение через copy + update
    c_update = merge_with_update(a, b)
    print(f"2. Копия + update:         {c_update}")

    # Проверка, что исходные словари не изменились
    print(f"\nИсходные словари остались без изменений:")
    print(f"  a = {a}")
    print(f"  b = {b}")

    # Демонстрация перезаписи при совпадении ключей
    a_overlap = {1: 'a', 2: 'b'}
    b_overlap = {2: 'x', 3: 'c'}
    merged_overlap = merge_with_unpacking(a_overlap, b_overlap)
    print(f"\nПри совпадении ключа 2:")
    print(f"  a = {a_overlap}")
    print(f"  b = {b_overlap}")
    print(f"  Результат: {merged_overlap} (значение из b перезаписывает a)")

    # Если Python 3.9+, можно использовать оператор |
    if sys.version_info >= (3, 9):
        print(f"\nВаш Python {sys.version_info.major}.{sys.version_info.minor} поддерживает оператор |")
        print(f"  Результат a | b: {a | b}")
    else:
        print(f"\nВаш Python {sys.version_info.major}.{sys.version_info.minor} не поддерживает оператор | (нужен 3.9+)")
