#!/usr/bin/env python3
"""
Task: Find the largest prime factor of a given number.
Problem: Project Euler #3 (https://projecteuler.net/problem=3)
Run: python3 largest_prime_factor.py
Status: Done
"""


def largest_prime_factor(n: int) -> int:
    """
    Возвращает наибольший простой делитель числа n.

    Алгоритм:
    1. Делим n на 2, пока оно чётное.
    2. Затем проверяем нечётные делители от 3 до sqrt(n).
    3. Если после делений остаётся число > 1, оно само является простым делителем.

    Args:
        n: Целое положительное число (n >= 2).

    Returns:
        Наибольший простой делитель.

    Examples:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(8)
        2
    """
    if n < 2:
        return n

    # Удаляем все множители 2
    while n % 2 == 0:
        n //= 2

    # Если n стал 1, то все делители были 2
    if n == 1:
        return 2

    # Проверяем нечётные делители до sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            n //= factor
        factor += 2

    # Если осталось число > 1, оно простое
    return n if n > 1 else 2


def largest_prime_factor_alternative(n: int) -> int:
    """
    Альтернативная реализация с перебором делителей от 2 до sqrt(n).
    Менее эффективна, но более читаема.
    """
    if n < 2:
        return n

    largest = 1
    # Перебираем возможные делители
    i = 2
    while i * i <= n:
        while n % i == 0:
            largest = i
            n //= i
        i += 1 if i == 2 else 2  # после 2 переходим к нечётным

    # Если осталось простое число больше 1
    if n > 1:
        largest = n
    return largest


def main() -> None:
    """Демонстрация работы на тестовых числах."""
    # Проверка на числе из условия
    test_num = 13195
    result = largest_prime_factor(test_num)
    print(f"Наибольший простой делитель числа {test_num} = {result}")
    assert result == 29, "Тест не пройден!"

    # Решение задачи
    target = 600851475143
    result_target = largest_prime_factor(target)
    print(f"Наибольший простой делитель числа {target} = {result_target}")

    # Сравнение с альтернативным методом
    assert largest_prime_factor(target) == largest_prime_factor_alternative(target)
    print("✅ Оба метода дают одинаковый результат.")


if __name__ == "__main__":
    main()
