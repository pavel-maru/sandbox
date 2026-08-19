#!/usr/bin/env python3
"""
Task: Generate all combinations of a given length from any set of symbols.
Run: python3 combinations_generator.py
Status: Done
"""

import itertools
from typing import Union, List, Iterable


def generate_combinations(
    symbols: Union[str, List[str], tuple],
    length: int
) -> List[str]:
    """
    Генерирует все комбинации длины `length` из переданных символов.
    Поддерживает любые символы: цифры, буквы, специальные знаки, эмодзи и т.д.

    Args:
        symbols: Набор символов (строка, список или кортеж).
        length: Длина каждой комбинации.

    Returns:
        Список строк, каждая строка — комбинация.

    Examples:
        >>> generate_combinations('01', 2)
        ['00', '01', '10', '11']
        >>> generate_combinations(['A', 'C', 'G', 'T'], 2)
        ['AA', 'AC', 'AG', 'AT', 'CA', 'CC', 'CG', 'CT', ...]
    """
    if length <= 0:
        return [""]
    # Преобразуем в список, чтобы итерация работала для любых типов
    sym_list = list(symbols)
    return [''.join(p) for p in itertools.product(sym_list, repeat=length)]


def generate_combinations_recursive(
    symbols: Union[str, List[str], tuple],
    length: int,
    prefix: str = ""
) -> List[str]:
    """
    Рекурсивная версия (для демонстрации).
    """
    if length == 0:
        return [prefix]
    result = []
    for ch in symbols:
        result.extend(generate_combinations_recursive(symbols, length - 1, prefix + ch))
    return result


def print_combinations(combinations: List[str], start_index: int = 1) -> None:
    """
    Печатает комбинации с нумерацией.

    Args:
        combinations: Список комбинаций (строк).
        start_index: Начальный номер (по умолчанию 1).
    """
    for i, comb in enumerate(combinations, start=start_index):
        print(f"{i}: {comb}")


def main() -> None:
    """Демонстрация работы с разными наборами символов."""
    # Пример 1: цифры (исходный вариант)
    symbols1 = '0123'
    length1 = 3
    print(f"Комбинации из символов '{symbols1}' длиной {length1}:")
    combs1 = generate_combinations(symbols1, length1)
    print_combinations(combs1)
    print(f"Всего: {len(combs1)}\n")

    # Пример 2: нуклеотиды (A, C, G, T) — как вы просили
    symbols2 = ['A', 'C', 'G', 'T']
    length2 = 3
    print(f"Комбинации нуклеотидов {symbols2} длиной {length2}:")
    combs2 = generate_combinations(symbols2, length2)
    # Покажем только первые 10, чтобы не засорять вывод
    for i, comb in enumerate(combs2[:10], start=1):
        print(f"{i}: {comb}")
    print(f"... (всего {len(combs2)} комбинаций)\n")

    # Пример 3: любой другой набор (например, символы '+', '-', '*')
    symbols3 = '+-*/'
    length3 = 2
    combs3 = generate_combinations(symbols3, length3)
    print(f"Комбинации из символов '{symbols3}' длиной {length3}:")
    print_combinations(combs3, start_index=0)  # нумерация с 0
    print(f"Всего: {len(combs3)}")

    # Проверка корректности рекурсивной версии
    assert generate_combinations(symbols1, length1) == generate_combinations_recursive(symbols1, length1)
    print("\n✅ Все версии (itertools и рекурсия) дают одинаковые результаты.")


if __name__ == "__main__":
    main()
