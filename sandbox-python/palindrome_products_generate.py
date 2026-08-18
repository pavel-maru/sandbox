#!/usr/bin/env python3
"""
Task: Find all palindromic products of two N-digit numbers.
Method: Generate palindromes in the product range and factor them.
Run: python3 palindrome_products_generate.py
Status: Done
"""

import time
import math
from typing import List, Dict, Tuple, Optional


def generate_palindromes_by_digits(digits: int) -> List[int]:
    """
    Генерирует все палиндромы с заданным количеством цифр.
    """
    if digits <= 0:
        return []
    palindromes = []
    half_len = (digits + 1) // 2
    start = 10 ** (half_len - 1)
    end = 10 ** half_len
    for half in range(start, end):
        half_str = str(half)
        if digits % 2 == 0:
            full_str = half_str + half_str[::-1]
        else:
            full_str = half_str + half_str[-2::-1]
        pal = int(full_str)
        palindromes.append(pal)
    return palindromes


def factor_palindrome(pal: int, n: int) -> Optional[Tuple[int, int]]:
    """
    Ищет разложение палиндрома на два n-значных множителя.
    Возвращает (a, b) или None.
    """
    min_factor = 10 ** (n - 1)
    max_factor = 10 ** n - 1
    limit = math.isqrt(pal)
    for a in range(min_factor, min(limit, max_factor) + 1):
        if pal % a == 0:
            b = pal // a
            if min_factor <= b <= max_factor:
                return (a, b)
    return None


def find_palindrome_products_generated(n: int) -> Dict[int, Tuple[int, int]]:
    """
    Основная функция: генерирует все палиндромы в диапазоне произведений
    и разлагает их на множители.
    """
    # Корректный диапазон произведений двух n-значных чисел
    min_product = 10 ** (2 * n - 2)   # например, для n=3: 10000
    max_product = 10 ** (2 * n) - 1   # например, 999999

    # Определяем количество цифр в диапазоне
    min_digits = len(str(min_product))
    max_digits = len(str(max_product))

    palindromes = []
    for digits in range(min_digits, max_digits + 1):
        pals = generate_palindromes_by_digits(digits)
        for p in pals:
            if min_product <= p <= max_product:
                palindromes.append(p)
    palindromes.sort()

    result = {}
    for p in palindromes:
        factors = factor_palindrome(p, n)
        if factors:
            result[p] = factors
    return result


def main() -> None:
    n = 3
    print(f"Поиск палиндромов-произведений для {n}-значных чисел")
    print("Метод: генерация палиндромов и поиск делителей")

    start = time.time()
    palindromes = find_palindrome_products_generated(n)
    elapsed = time.time() - start

    print(f"Найдено палиндромов: {len(palindromes)}")
    print(f"Время выполнения: {elapsed:.4f} сек")

    print("\nПримеры (первые 5):")
    for i, (prod, (a, b)) in enumerate(palindromes.items()):
        if i >= 5:
            break
        print(f"  {a} × {b} = {prod}")


if __name__ == "__main__":
    main()
