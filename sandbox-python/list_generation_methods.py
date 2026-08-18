#!/usr/bin/env python3
"""
Task: Generate a list of numbers from 2 to 29 with step 3 using three different methods.
Run: python3 list_generation_methods.py
Status: Done
"""

from typing import List


def generate_with_unpacking(start: int, stop: int, step: int) -> List[int]:
    """
    Использует распаковку оператором * внутри списка.
    
    Args:
        start: Начальное число (включительно).
        stop: Конечное число (не включается).
        step: Шаг.
    
    Returns:
        Список чисел.
    """
    return [*range(start, stop, step)]


def generate_with_comprehension(start: int, stop: int, step: int) -> List[int]:
    """
    Использует генератор списка (list comprehension).
    
    Args:
        start: Начальное число (включительно).
        stop: Конечное число (не включается).
        step: Шаг.
    
    Returns:
        Список чисел.
    """
    return [x for x in range(start, stop, step)]


def generate_with_list_constructor(start: int, stop: int, step: int) -> List[int]:
    """
    Использует конструктор list(), принимающий итерируемый объект.
    
    Args:
        start: Начальное число (включительно).
        stop: Конечное число (не включается).
        step: Шаг.
    
    Returns:
        Список чисел.
    """
    return list(range(start, stop, step))


if __name__ == "__main__":
    start, stop, step = 2, 30, 3
    
    print(f"Генерация списка от {start} до {stop-1} с шагом {step}:\n")
    
    result1 = generate_with_unpacking(start, stop, step)
    print(f"1. Распаковка *range:  {result1}")
    
    result2 = generate_with_comprehension(start, stop, step)
    print(f"2. Генератор списка:    {result2}")
    
    result3 = generate_with_list_constructor(start, stop, step)
    print(f"3. Конструктор list():  {result3}")
    
    # Проверка, что все результаты одинаковы
    assert result1 == result2 == result3, "Результаты различаются!"
    print("\n✅ Все три способа дают одинаковый результат.")
    
    # Дополнительно: сравнение производительности (можно раскомментировать)
    # import timeit
    # print("\nСравнение производительности (10000 повторений):")
    # for func in [generate_with_unpacking, generate_with_comprehension, generate_with_list_constructor]:
    #     t = timeit.timeit(lambda: func(start, stop, step), number=10000)
    #     print(f"{func.__name__}: {t:.5f} сек")
