#!/usr/bin/env python3
"""
Task: Display animal emojis using Unicode names and direct symbols.
Run: python3 animal_emoji_demo.py
Status: Done
"""

import unicodedata


def print_animal_emojis_named() -> None:
    """
    Выводит эмодзи животных, используя стандартные имена Unicode.
    Имена чувствительны к регистру, здесь они приведены в верхнем регистре.
    """
    animals = [
        'SNAKE',
        'RABBIT',
        'BIRD',
        'PARROT',
        'DUCK',
        'DOG',
        'CAT',
        'BEETLE',
        'BUTTERFLY',
        'MOUSE',
        'RAT'
    ]
    for name in animals:
        try:
            # Получаем символ по имени
            char = unicodedata.lookup(name)
            print(char, end=' ')
        except KeyError:
            print(f'[Unknown: {name}]', end=' ')
    print()


def print_animal_emojis_direct() -> None:
    """Выводит те же эмодзи, но прямым вставлением символов."""
    direct_animals = [
        '🐍',   # змея
        '🐇',   # кролик
        '🐦',   # птица
        '🦜',   # попугай
        '🦆',   # утка
        '🐕',   # собака
        '🐈',   # кот
        '🐞',   # жук
        '🦋',   # бабочка
        '🐁',   # мышь
        '🐀'    # крыса
    ]
    print(' '.join(direct_animals))


def main() -> None:
    """Демонстрация обоих способов."""
    print("Эмодзи животных через unicodedata.lookup():")
    print_animal_emojis_named()

    print("\nПрямой ввод эмодзи (альтернативный способ):")
    print_animal_emojis_direct()


if __name__ == "__main__":
    main()
