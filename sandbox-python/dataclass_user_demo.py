#!/usr/bin/env python3
"""
Task: Demonstrate dataclass usage and dynamic attribute assignment.
Run: python3 dataclass_user_demo.py
Status: Done
"""

from dataclasses import dataclass


@dataclass
class User:
    """
    Класс пользователя с двумя обязательными полями.

    Attributes:
        name (str): Имя пользователя.
        age (int): Возраст пользователя.
    """
    name: str
    age: int


if __name__ == "__main__":
    # Создание экземпляра
    person = User('Alex', 25)
    print(f"Имя: {person.name}")
    print(f"Возраст: {person.age}")

    # Динамическое добавление нового атрибута (работает, т.к. dataclass не использует __slots__)
    person.surname = 'Smith'
    print(f"Фамилия (добавлена динамически): {person.surname}")

    # Важно: добавленный атрибут не входит в определение класса
    # и не участвует в сравнении или repr (если не переопределить)
    print(f"\nОбъект целиком: {person}")
    print(f"Поля, определённые в dataclass: {person.__dataclass_fields__.keys()}")
    print(f"Все атрибуты объекта: {person.__dict__.keys()}")

    # Рекомендация: если нужно запретить динамические атрибуты,
    # используйте параметр slots=True в dataclass (Python 3.10+):
    #
    # @dataclass(slots=True)
    # class UserSlots:
    #     name: str
    #     age: int
    #
    # Тогда добавление surname вызовет AttributeError.
