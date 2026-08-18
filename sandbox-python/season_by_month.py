#!/usr/bin/env python3
"""
Task: Determine the season (winter, spring, summer, autumn) by month number.
Run: python3 season_by_month.py
Status: Done
"""

from typing import Optional

# Прямой словарь: кортеж месяцев → сезон
SEASONS_MAP = {
    (12, 1, 2): 'winter',
    (3, 4, 5): 'spring',
    (6, 7, 8): 'summer',
    (9, 10, 11): 'autumn'
}


def get_season(month: int) -> Optional[str]:
    """
    Возвращает название времени года по номеру месяца.

    Args:
        month: Номер месяца (1–12).

    Returns:
        Название сезона (зима, весна, лето, осень) или None, если месяц некорректен.

    Examples:
        >>> get_season(1)
        'winter'
        >>> get_season(6)
        'summer'
    """
    if not 1 <= month <= 12:
        return None

    for months, season in SEASONS_MAP.items():
        if month in months:
            return season
    return None  # на случай, если не найдено (не должно произойти)


def main() -> None:
    """Демонстрация работы."""
    test_months = [1, 3, 6, 9, 12, 13]
    for m in test_months:
        season = get_season(m)
        if season:
            print(f"Месяц {m:2d} → {season}")
        else:
            print(f"Месяц {m:2d} → некорректный номер")


if __name__ == "__main__":
    main()
