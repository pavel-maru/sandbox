# Sandbox — коллекция учебных программ на Python и C

Этот репозиторий содержит небольшие самодостаточные программы, написанные в процессе изучения языков программирования. Здесь собраны алгоритмические задачи, демонстрации различных подходов и полезные сниппеты.

Каждый файл задокументирован, снабжён комментариями и инструкциями по запуску.

---

## Структура

- `sandbox-python/` — программы на Python 3
- `sandbox-c/` — программы на C (стандарт C11)

---

## Программы на Python

| Файл | Описание | Запуск |
|------|----------|--------|
| `alphabet_positions.py` | Номера букв в алфавите (рус./англ.) | `python3 alphabet_positions.py` |
| `combinations_generator.py` | Генерация комбинаций из символов | `python3 combinations_generator.py` |
| `cyclic_repeat_string.py` | Циклическое повторение строки | `python3 cyclic_repeat_string.py` |
| `dataclass_user_demo.py` | Демонстрация `dataclass` | `python3 dataclass_user_demo.py` |
| `dict_comprehension_invert.py` | Генерация и инверсия словаря | `python3 dict_comprehension_invert.py` |
| `dict_merge_unpack.py` | Объединение словарей | `python3 dict_merge_unpack.py` |
| `euler001_multiples_of_3_and_5.py` | Сумма кратных 3 или 5 (Project Euler #1) | `python3 euler001_multiples_of_3_and_5.py` |
| `eval_sum_expression.py` | Вычисление `0+1+...+n-1` через `eval()` | `python3 eval_sum_expression.py` |
| `extract_digits_to_int.py` | Извлечение числа из строки | `python3 extract_digits_to_int.py` |
| `file_write_read_demo.py` | Запись и чтение файла | `python3 file_write_read_demo.py` |
| `find_char_positions.py` | Поиск позиций символа | `python3 find_char_positions.py` |
| `fizzbuzz_variants.py` | Четыре варианта FizzBuzz | `python3 fizzbuzz_variants.py` |
| `invert_dict.py` | Обмен ключей и значений | `python3 invert_dict.py` |
| `largest_prime_factor.py` | Наибольший простой делитель | `python3 largest_prime_factor.py` |
| `letter_count_and_positions.py` | Подсчёт букв и их позиций | `python3 letter_count_and_positions.py` |
| `list_generation_methods.py` | Три способа создания списка | `python3 list_generation_methods.py` |
| `list_mutation_demo.py` | Мутация списка в функции | `python3 list_mutation_demo.py` |
| `palindrome_products.py` | Палиндромы-произведения (брутфорс) | `python3 palindrome_products.py` |
| `palindrome_products_generate.py` | Оптимизированная генерация | `python3 palindrome_products_generate.py` |
| `prime_numbers_sieve.py` | Простые числа (решето) | `python3 prime_numbers_sieve.py` |
| `replace_single_asterisk.py` | Замена `*` на `!` | `python3 replace_single_asterisk.py` |
| `reverse_sequence.py` | Переворот кортежа/списка | `python3 reverse_sequence.py` |
| `reverse_string_generator.py` | Разворот строки генератором | `python3 reverse_string_generator.py` |
| `season_by_month.py` | Время года по номеру месяца | `python3 season_by_month.py` |
| `sum_of_cubes_digit_sum_divisible_by_7.py` | Сумма кубов с условием | `python3 sum_of_cubes_digit_sum_divisible_by_7.py` |
| `text_cleaner.py` | Очистка текстовых файлов | `python3 text_cleaner.py <входной_файл> [выходной]` |

---

## Программы на C

| Файл | Описание | Сборка и запуск |
|------|----------|-----------------|
| `palindrome_index.c` | Проверка палиндрома (индексы) | `gcc -std=c11 palindrome_index.c -o palindrome_index && ./palindrome_index` |
| `palindrome_pointer.c` | Проверка палиндрома (указатели) | `gcc -std=c11 palindrome_pointer.c -o palindrome_pointer && ./palindrome_pointer` |
| `palindrome_manual.c` | Проверка палиндрома (посимвольно) | `gcc -std=c11 palindrome_manual.c -o palindrome_manual && ./palindrome_manual` |
| `rad_to_deg.c` | Перевод радиан в градусы | `gcc -std=c11 rad_to_deg.c -lm -o rad_to_deg && ./rad_to_deg` |
| `remove_last_substr_strstr.c` | Удаление подстроки (strstr) | `gcc -std=c11 remove_last_substr_strstr.c -o remove_last_substr_strstr && ./remove_last_substr_strstr` |
| `remove_last_substr_manual.c` | Удаление подстроки (ручной) | `gcc -std=c11 remove_last_substr_manual.c -o remove_last_substr_manual && ./remove_last_substr_manual` |
| `groot.c` | Вывод "I'm Groot." | `gcc -std=c11 groot.c -o groot && ./groot` |
| `binomial_coefficients.c` | Биномиальные коэффициенты | `gcc -std=c11 binomial_coefficients.c -o binomial_coefficients && ./binomial_coefficients` |
| `max_before_minus_one.c` | Максимум до -1 | `gcc -std=c11 max_before_minus_one.c -o max_before_minus_one && ./max_before_minus_one` |

---

## Требования

- **Python**: версия 3.6 или выше (рекомендуется 3.10+). Все программы используют только стандартную библиотеку.
- **C**: компилятор с поддержкой C11 (например, `gcc` или `clang`). Для `rad_to_deg.c` требуется линковка с математической библиотекой (`-lm`).

---

## Как использовать

1. Клонируйте репозиторий:

git clone https://github.com/pavel-maru/sandbox.git
cd sandbox

2. Для Python-программ перейдите в папку `sandbox-python/` и выполните:

python3 имя_файла.py

3. Для C-программ перейдите в папку `sandbox-c/` и скомпилируйте:

gcc -std=c11 -Wall -Wextra -O2 имя_файла.c -o имя_файла
./имя_файла

---

## Оформление кода

Все файлы соответствуют единым стандартам:
- Документация в формате docstring (Python) или Doxygen-стиль (C).
- Обработка ошибок ввода и краевых случаев.
- Соблюдение стилей: PEP 8 для Python, K&R для C.
- Каждый файл самодостаточен и не требует внешних зависимостей (кроме стандартной библиотеки).

---

## Лицензия

Этот репозиторий распространяется под лицензией MIT. Вы можете свободно использовать, модифицировать и распространять код с указанием авторства.

Подробнее: [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT)

---

**Автор:** [pavel-maru]
**Репозиторий:** [https://github.com/pavel-maru/sandbox](https://github.com/pavel-maru/sandbox)
