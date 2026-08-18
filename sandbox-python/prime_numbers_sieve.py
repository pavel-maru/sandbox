#!/usr/bin/env python3
"""
Task: Find all prime numbers up to N using two methods.
Run: python3 prime_numbers_sieve.py
Status: Done
"""


def primes_naive(limit: int) -> list[int]:
    """
    Находит все простые числа до limit методом перебора делителей.
    Для каждого числа проверяем, делится ли оно на уже найденные простые.

    Args:
        limit: Верхняя граница (включительно).

    Returns:
        Список простых чисел.
    """
    if limit < 2:
        return []
    primes = [2]
    for num in range(3, limit + 1):
        is_prime = True
        for p in primes:
            if p * p > num:   # оптимизация: проверяем только до sqrt(num)
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def primes_sieve(limit: int) -> list[int]:
    """
    Находит все простые числа до limit с помощью решета Эратосфена.
    Быстрее для больших limit.

    Args:
        limit: Верхняя граница.

    Returns:
        Список простых чисел.
    """
    if limit < 2:
        return []
    # Изначально все числа считаем простыми
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            # Вычёркиваем кратные i, начиная с i*i
            step = i
            start = i * i
            sieve[start:limit+1:step] = [False] * ((limit - start) // step + 1)
    return [i for i, is_prime in enumerate(sieve) if is_prime]


def main() -> None:
    """Демонстрация работы."""
    N = 30
    print(f"Простые числа до {N}:")

    # Метод 1: наивный перебор
    naive = primes_naive(N)
    print(f"  Наивный перебор: {naive}")

    # Метод 2: решето Эратосфена
    sieve = primes_sieve(N)
    print(f"  Решето Эратосфена: {sieve}")

    # Проверка, что результаты совпадают
    assert naive == sieve
    print("✅ Оба метода дают одинаковый результат.")


if __name__ == "__main__":
    main()
