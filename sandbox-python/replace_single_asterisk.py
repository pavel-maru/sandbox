#!/usr/bin/env python3
"""
Task: Replace single asterisks '*' with '!' but keep '**' unchanged.
Run: python3 replace_single_asterisk.py
Status: Done
"""

import re
from typing import Optional


def replace_single_asterisk_with_replace(text: str) -> str:
    """
    Реализация через последовательные замены: сначала все '*' → '!',
    затем '!!' → '**' (восстанавливаем двойные звёздочки).

    Args:
        text: Исходная строка.

    Returns:
        Строка с заменёнными одиночными звёздочками.

    Note:
        Этот метод прост, но имеет побочный эффект: если в исходной строке
        было три звёздочки подряд ('***'), они превратятся в '**!' (т.е.
        первые две станут '**', последняя - '!'). Это может быть желаемым
        или нет в зависимости от задачи.
    """
    replaced = text.replace('*', '!')   # все '*' становятся '!'
    restored = replaced.replace('!!', '**')  # возвращаем '!!' обратно в '**'
    return restored


def replace_single_asterisk_regex(text: str) -> str:
    """
    Реализация через регулярное выражение: заменяем '*', которые не являются
    частью '**' (т.е. одиночные звёздочки, не стоящие рядом с другой звёздочкой).

    Используем negative lookbehind и lookahead, чтобы избежать замены в паре.

    Args:
        text: Исходная строка.

    Returns:
        Строка с заменёнными одиночными звёздочками.
    """
    # Паттерн: звёздочка, перед которой нет звёздочки, и после которой нет звёздочки
    # (?<!\*) - негативный просмотр назад (не перед звёздочкой)
    # (?!\*)  - негативный просмотр вперёд (не после звёздочки)
    pattern = r'(?<!\*)\*(?!\*)'
    return re.sub(pattern, '!', text)


if __name__ == "__main__":
    test_string = 'aaa ** bbb * ccc * ddd **'
    print(f"Исходная строка:  {test_string}")
    
    result1 = replace_single_asterisk_with_replace(test_string)
    print(f"Замена через replace: {result1}")
    
    result2 = replace_single_asterisk_regex(test_string)
    print(f"Замена через regex:    {result2}")

    # Тест с тремя звёздочками
    test3 = '***'
    print(f"\nТест с тремя звёздочками: '{test3}'")
    print(f"  replace: {replace_single_asterisk_with_replace(test3)}")
    print(f"  regex:   {replace_single_asterisk_regex(test3)}")

    # Пустая строка
    empty = ''
    print(f"\nПустая строка: '{empty}' -> '{replace_single_asterisk_regex(empty)}'")
