#!/usr/bin/env python3
"""
Task: Repeat a string cyclically to reach a specified length (float multiplier).
Run: python3 cyclic_repeat_string.py
Status: Done
"""

import itertools
from typing import Optional

def repeat_to_length(text: str, multiplier: float) -> Optional[str]:
    """
    Повторяет строку циклически, чтобы итоговая длина была примерно len(text)*multiplier.

    Args:
        text: Исходная строка.
        multiplier: Коэффициент длины (может быть дробным).

    Returns:
        Новая строка длиной int(len(text)*multiplier) или None, если multiplier <= 0.
    """
    if multiplier <= 0:
        return None
    target_length = int(len(text) * multiplier)
    if target_length == 0:
        return ""
    cycle = itertools.cycle(text)
    return ''.join(next(cycle) for _ in range(target_length))

if __name__ == "__main__":
    sample = "Hello"
    factor = 2.7
    result = repeat_to_length(sample, factor)
    print(f"Исходная строка: '{sample}' (длина {len(sample)})")
    print(f"Коэффициент: {factor}")
    print(f"Результат: '{result}' (длина {len(result)})")
