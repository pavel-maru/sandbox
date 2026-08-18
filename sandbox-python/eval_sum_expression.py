#!/usr/bin/env python3
"""
Task: Evaluate a string expression built as sum of numbers from 0 to n-1.
Run: python3 eval_sum_expression.py
Status: Done
"""

def evaluate_sum_expression(n: int) -> int:
    """
    Строит строку вида '0+1+2+...+n-1' и вычисляет её через eval().

    Args:
        n: Количество слагаемых (начиная с 0).

    Returns:
        Результат вычисления (сумма арифметической прогрессии).

    Raises:
        ValueError: если n <= 0.
    """
    if n <= 0:
        raise ValueError("n должно быть положительным")
    expr = '+'.join(str(i) for i in range(n))
    return eval(expr)   # Безопасно, т.к. выражение создано нами

if __name__ == "__main__":
    n = 5
    result = evaluate_sum_expression(n)
    print(f"Строка выражения: {'+'.join(str(i) for i in range(n))}")
    print(f"Результат eval: {result}")
