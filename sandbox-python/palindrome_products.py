#!/usr/bin/env python3
"""
Task: Find all palindromic products of two N-digit numbers.
Contains three palindrome check implementations for comparison.
Run: python3 palindrome_products.py
Status: Done
"""

import time
from typing import Dict, Tuple, Callable


# ----- Реализации проверки палиндрома -----

def is_palindrome_string(num: int) -> bool:
    """Строковая проверка (через срез)."""
    s = str(num)
    return s == s[::-1]


def is_palindrome_number_full(num: int) -> bool:
    """Числовая проверка (полный разворот)."""
    if num < 0:
        return False
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return original == rev


def is_palindrome_number_half(num: int) -> bool:
    """
    Числовая проверка с разворотом только половины числа (ранний выход).
    Корректно работает для любых неотрицательных чисел (включая оканчивающиеся на 0).
    """
    if num < 0:
        return False
    if num == 0:
        return True
    # Числа, оканчивающиеся на 0 (кроме 0), не могут быть палиндромами
    if num % 10 == 0:
        return False
    rev = 0
    while num > rev:
        rev = rev * 10 + num % 10
        num //= 10
    # Для нечётного количества цифр отбрасываем среднюю
    return num == rev or num == rev // 10


# ----- Поиск палиндромов с выбором метода -----

def find_palindrome_products(n: int, check_func: Callable[[int], bool]) -> Dict[int, Tuple[int, int]]:
    start = 10 ** (n - 1)
    end = 10 ** n
    result = {}
    for a in range(start, end):
        for b in range(a, end):
            product = a * b
            if check_func(product) and product not in result:
                result[product] = (a, b)
    return result


# ----- Демонстрация и сравнение -----

def main():
    n = 3
    print(f"Поиск палиндромов для {n}-значных чисел (от {10**(n-1)} до {10**n - 1})\n")

    methods = [
        ("Строковая", is_palindrome_string),
        ("Числовая (полный разворот)", is_palindrome_number_full),
        ("Числовая (половинный разворот)", is_palindrome_number_half),
    ]

    results = {}
    for name, func in methods:
        start = time.time()
        res = find_palindrome_products(n, func)
        elapsed = time.time() - start
        results[name] = (res, elapsed)
        print(f"{name}: {len(res)} палиндромов, время {elapsed:.4f} сек")

    # Проверяем, что все результаты одинаковы
    first_result = results[methods[0][0]][0]
    for name, (res, _) in results.items():
        if res != first_result:
            print(f"⚠️ Результаты для {name} отличаются!")
        else:
            print(f"✅ {name} даёт совпадающие результаты")

    # Покажем первые 5
    print("\nПримеры (первые 5):")
    for i, (prod, (a, b)) in enumerate(first_result.items()):
        if i >= 5:
            break
        print(f"  {a} × {b} = {prod}")


if __name__ == "__main__":
    main()
