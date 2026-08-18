#!/usr/bin/env python3
"""
Task: Find the sum of all multiples of 3 or 5 below 1000.
Project Euler Problem 1.
Run: python3 euler001_multiples_of_3_and_5.py
Status: Done
"""


def sum_multiples_loop(limit: int) -> int:
    """
    Решение через цикл с проверкой условия.
    Явный, понятный способ.

    Args:
        limit: Верхняя граница (не включается).

    Returns:
        Сумма чисел < limit, кратных 3 или 5.
    """
    total = 0
    for num in range(1, limit):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total


def sum_multiples_generator(limit: int) -> int:
    """
    Решение через генератор списка и встроенную сумму.
    Более питоновский стиль.

    Args:
        limit: Верхняя граница.

    Returns:
        Сумма чисел < limit, кратных 3 или 5.
    """
    return sum(num for num in range(1, limit) if num % 3 == 0 or num % 5 == 0)


def sum_multiples_formula(limit: int) -> int:
    """
    Решение через формулу суммы арифметической прогрессии.
    Самый быстрый способ (O(1)).
    Сумма чисел, кратных k: k * (1 + 2 + ... + m), где m = (limit-1)//k.
    Используем принцип включения-исключения.

    Args:
        limit: Верхняя граница.

    Returns:
        Сумма чисел < limit, кратных 3 или 5.
    """
    def sum_divisible_by(k: int) -> int:
        count = (limit - 1) // k
        return k * count * (count + 1) // 2

    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)


def main() -> None:
    """Демонстрация работы всех трёх методов."""
    N = 1000

    print(f"Сумма чисел < {N}, кратных 3 или 5:")
    print(f"  Цикл:          {sum_multiples_loop(N)}")
    print(f"  Генератор:     {sum_multiples_generator(N)}")
    print(f"  Формула (O(1)): {sum_multiples_formula(N)}")

    # Проверка, что все результаты совпадают
    assert sum_multiples_loop(N) == sum_multiples_generator(N) == sum_multiples_formula(N)
    print("✅ Все методы дают одинаковый результат.")


if __name__ == "__main__":
    main()
