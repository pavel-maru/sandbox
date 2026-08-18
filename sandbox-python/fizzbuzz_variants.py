#!/usr/bin/env python3
"""
Task: Implement FizzBuzz in 4 different styles.
Run: python3 fizzbuzz_variants.py
Status: Done
"""

from typing import List, Union


def fizzbuzz_generator(n: int) -> List[Union[str, int]]:
    """
    Вариант 1: однострочный генератор с условными выражениями.
    Возвращает список строк или чисел.
    """
    return [
        'FizzBuzz' if i % 3 == 0 and i % 5 == 0 else
        'Fizz' if i % 3 == 0 else
        'Buzz' if i % 5 == 0 else
        i
        for i in range(1, n + 1)
    ]


def fizzbuzz_if_elif(n: int) -> List[Union[str, int]]:
    """
    Вариант 2: классический if-elif-else с присваиванием значения в переменную.
    """
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append('FizzBuzz')
        elif i % 3 == 0:
            result.append('Fizz')
        elif i % 5 == 0:
            result.append('Buzz')
        else:
            result.append(i)
    return result


def fizzbuzz_print_conditions(n: int) -> List[Union[str, int]]:
    """
    Вариант 3: печать по частям — сначала 'Fizz', потом 'Buzz', если нужно.
    Возвращает список собранных строк.
    """
    result = []
    for i in range(1, n + 1):
        output = ''
        if i % 3 == 0:
            output += 'Fizz'
        if i % 5 == 0:
            output += 'Buzz'
        if not output:          # если ничего не добавили
            output = str(i)
        result.append(output)
    return result


def fizzbuzz_not_operator(n: int) -> List[Union[str, int]]:
    """
    Вариант 4: использование `not` для краткости (not i%3 == True).
    Возвращает список.
    """
    result = []
    for i in range(1, n + 1):
        if not i % 3:
            fizz = 'Fizz'
        else:
            fizz = ''
        if not i % 5:
            buzz = 'Buzz'
        else:
            buzz = ''
        output = fizz + buzz
        if not output:
            output = i
        result.append(output)
    return result


def main() -> None:
    """Демонстрация всех четырёх вариантов."""
    n = 20  # можно менять, но для примера покажем только до 20, чтобы не засорять вывод
    print(f"FizzBuzz для чисел от 1 до {n}:\n")

    variants = [
        (fizzbuzz_generator, "Генератор (однострочник)"),
        (fizzbuzz_if_elif, "if-elif-else"),
        (fizzbuzz_print_conditions, "Печать по условиям"),
        (fizzbuzz_not_operator, "С использованием not")
    ]

    for func, desc in variants:
        result = func(n)
        # Преобразуем в строку для красивого вывода
        output_str = ' '.join(str(x) for x in result)
        print(f"{desc}:\n{output_str}\n")


if __name__ == "__main__":
    main()
