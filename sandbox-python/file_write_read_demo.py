#!/usr/bin/env python3
"""
Task: Write numbers 0..9 to a file (one per line), then read the first line.
Run: python3 file_write_read_demo.py
Status: Done
"""

import os
from typing import Optional


def write_numbers_to_file(filename: str, count: int) -> None:
    """
    Записывает числа от 0 до count-1 в файл, каждое на отдельной строке.

    Args:
        filename: Путь к файлу.
        count: Количество чисел (от 0 до count-1).

    Raises:
        OSError: Если не удаётся открыть файл для записи.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(count):
            file.write(f"{i}\n")


def read_first_line(filename: str) -> Optional[str]:
    """
    Читает первую строку из файла и возвращает её без символа перевода строки.

    Args:
        filename: Путь к файлу.

    Returns:
        Первая строка без '\n' или None, если файл пуст или не существует.

    Raises:
        OSError: При ошибках чтения файла.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            first_line = file.readline()
            if not first_line:
                return None
            return first_line.rstrip('\n')
    except FileNotFoundError:
        return None


def main() -> None:
    """Основная демонстрационная функция."""
    filename = "test.txt"
    count = 10

    write_numbers_to_file(filename, count)

    first_line = read_first_line(filename)
    if first_line is not None:
        print(f"Первая строка: '{first_line}'")
        print(f"Длина строки (без символа новой строки): {len(first_line)}")
    else:
        print("Файл пуст или не существует.")

    # Удаляем временный файл после завершения (опционально)
    try:
        os.remove(filename)
        print(f"Временный файл '{filename}' удалён.")
    except OSError:
        pass  # Если файл не удалось удалить — не критично


if __name__ == "__main__":
    main()
