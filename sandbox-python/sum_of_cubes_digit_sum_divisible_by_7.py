#!/usr/bin/env python3
"""
Task: Find the sum of cubes of numbers from 1 to 1000 such that the sum of digits of the cube is divisible by 7.
Run: python3 sum_of_cubes_digit_sum_divisible_by_7.py
Status: Done
"""


def digit_sum(num: int) -> int:
    """
    Вычисляет сумму цифр целого неотрицательного числа.
    Использует арифметику (без преобразования в строку).

    Args:
        num: Число для обработки.

    Returns:
        Сумма цифр числа.
    """
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


def sum_cubes_condition(limit: int) -> int:
    """
    Вычисляет сумму кубов чисел от 1 до limit, у которых сумма цифр куба делится на 7.

    Args:
        limit: Верхняя граница (включительно).

    Returns:
        Сумма кубов всех чисел, удовлетворяющих условию.
    """
    total = 0
    for i in range(1, limit + 1):
        cube = i ** 3
        if digit_sum(cube) % 7 == 0:
            total += cube
    return total


def sum_cubes_condition_generator(limit: int) -> int:
    """
    То же самое, но с использованием генератора списка и встроенной суммы.
    """
    return sum(
        i ** 3
        for i in range(1, limit + 1)
        if digit_sum(i ** 3) % 7 == 0
    )


def main() -> None:
    """Демонстрация работы."""
    N = 1000

    result = sum_cubes_condition(N)
    print(f"Сумма кубов чисел от 1 до {N}, сумма цифр куба кратна 7:")
    print(f"  {result}")

    # Проверка, что оба метода дают одинаковый результат
    assert sum_cubes_condition(N) == sum_cubes_condition_generator(N)
    print("✅ Оба подхода (цикл и генератор) дают одинаковый результат.")


if __name__ == "__main__":
    main()
