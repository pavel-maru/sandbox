#!/usr/bin/env python3
"""
Task: Invert a dictionary (swap keys and values).
Run: python3 invert_dict.py
Status: Done
"""

from typing import Dict, Hashable, Any

def invert_dictionary(original: Dict[Hashable, Any]) -> Dict[Any, Hashable]:
    """
    Меняет местами ключи и значения словаря.

    Args:
        original: Исходный словарь, где ключи хешируемы, значения также хешируемы.

    Returns:
        Новый словарь, где ключи — старые значения, а значения — старые ключи.

    Note:
        Если в исходном словаре есть повторяющиеся значения, они будут перезаписаны.
    """
    return {value: key for key, value in original.items()}

if __name__ == "__main__":
    seasons = {
        'winter': (12, 1, 2),
        'spring': (3, 4, 5),
        'summer': (6, 7, 8),
        'autumn': (9, 10, 11)
    }
    inverted = invert_dictionary(seasons)
    print("Исходный словарь:")
    for season, months in seasons.items():
        print(f"  {season}: {months}")
    print("\nИнвертированный словарь:")
    for months, season in inverted.items():
        print(f"  {months}: {season}")
