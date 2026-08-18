#!/usr/bin/env python3
"""
Task: Reverse a tuple/list using slicing.
Run: python3 reverse_sequence.py
Status: Done
"""

from typing import Sequence, TypeVar

T = TypeVar('T')

def reverse_sequence(seq: Sequence[T]) -> Sequence[T]:
    """
    Возвращает перевёрнутую копию последовательности (кортеж, список, строка).

    Args:
        seq: Любая последовательность.

    Returns:
        Перевёрнутая последовательность того же типа.
    """
    return seq[::-1]

if __name__ == "__main__":
    original = (0, 1, 2, 3, 4, 5)
    reversed_tuple = reverse_sequence(original)
    print(f"Исходный кортеж: {original}")
    print(f"Перевёрнутый: {reversed_tuple}")
