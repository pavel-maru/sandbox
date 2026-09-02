#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модуль для очистки текстовых файлов от нежелательных символов.

Оставляет только:
- буквы (любого алфавита),
- цифры,
- пробел ' ',
- разрешённые знаки препинания (задаются в ALLOWED_PUNCTUATION),
- символы перевода строки.

Всё остальное (табуляции, управляющие коды, стрелки и т.д.) удаляется.

Использование из командной строки:
    python3 text_cleaner.py <входной_файл> [выходной_файл]

Если выходной файл не указан, результат сохраняется с расширением .txt.
"""

import sys
import os
from typing import Set, Optional

# Набор разрешённых знаков препинания (можно редактировать)
ALLOWED_PUNCTUATION: Set[str] = set(".,!?;:-()[]{}'\"")


def clean_text(text: str, allowed_punct: Optional[Set[str]] = None) -> str:
    """
    Очищает строку, оставляя только разрешённые символы.

    Args:
        text (str): Исходная строка.
        allowed_punct (Optional[Set[str]]): Набор разрешённых знаков препинания.
            Если не указан, используется ALLOWED_PUNCTUATION.

    Returns:
        str: Очищенная строка.

    Example:
        >>> clean_text("Привет! Как дела? (хорошо)")
        'Привет! Как дела? (хорошо)'
        >>> clean_text("Текст с табуляцией\tи стрелкой →")
        'Текст с табуляциейи стрелкой'
    """
    if allowed_punct is None:
        allowed_punct = ALLOWED_PUNCTUATION

    result = []
    for ch in text:
        if (ch.isalpha() or ch.isdigit() or
                ch == ' ' or
                ch in allowed_punct or
                ch in '\n\r'):
            result.append(ch)
        # иначе – пропускаем (удаляем)
    return ''.join(result)


def process_file(input_path: str,
                 output_path: Optional[str] = None,
                 encoding: str = 'utf-8') -> str:
    """
    Читает файл, очищает содержимое и записывает в новый файл.

    Args:
        input_path (str): Путь к исходному файлу.
        output_path (Optional[str]): Путь для сохранения результата.
            Если не указан, к имени исходного файла добавляется .txt.
        encoding (str): Кодировка файла (по умолчанию utf-8).

    Returns:
        str: Путь к сохранённому файлу.

    Raises:
        FileNotFoundError: Если входной файл не найден.
        PermissionError: Если нет прав на чтение/запись.
        UnicodeDecodeError: Если файл не может быть прочитан в указанной кодировке.
    """
    if output_path is None:
        base, _ = os.path.splitext(input_path)
        output_path = base + '.txt'

    try:
        with open(input_path, 'r', encoding=encoding) as infile:
            with open(output_path, 'w', encoding=encoding) as outfile:
                for line in infile:
                    cleaned_line = clean_text(line)
                    outfile.write(cleaned_line)
    except FileNotFoundError:
        raise FileNotFoundError(f"Входной файл '{input_path}' не найден.")
    except PermissionError:
        raise PermissionError(f"Нет прав на чтение/запись файла '{input_path}'.")
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(
            f"Не удалось прочитать файл в кодировке {encoding}. "
            f"Попробуйте указать другую кодировку. Подробнее: {e}"
        )

    return output_path


def main() -> None:
    """Точка входа для командной строки."""
    if len(sys.argv) < 2:
        print("Использование: python3 text_cleaner.py <входной_файл> [выходной_файл]")
        print("Пример: python3 text_cleaner.py myfile.dat")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        result_path = process_file(input_file, output_file)
        print(f"Готово! Результат сохранён в: {result_path}")
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
