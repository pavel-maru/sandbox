# Sandbox — коллекция учебных программ на Python и C

Этот репозиторий содержит небольшие самодостаточные программы, написанные в процессе изучения языков программирования. Здесь собраны алгоритмические задачи, демонстрации различных подходов и полезные сниппеты.

Каждый файл задокументирован, снабжён комментариями и инструкциями по запуску.

---

## Структура

- `sandbox-python/` — программы на Python 3
- `sandbox-c/` — программы на C (стандарт C11)

---

## Программы на Python

- **`alphabet_positions.py`** — преобразование строки в номера букв алфавита (рус./англ.).
  Запуск: `python3 alphabet_positions.py`

- **`combinations_generator.py`** — генерация всех комбинаций из заданного набора символов (например, нуклеотиды).
  Запуск: `python3 combinations_generator.py`

- **`cyclic_repeat_string.py`** — циклическое повторение строки до нужной длины (с дробным коэффициентом).
  Запуск: `python3 cyclic_repeat_string.py`

- **`dataclass_user_demo.py`** — демонстрация `dataclass` и динамического добавления атрибутов.
  Запуск: `python3 dataclass_user_demo.py`

- **`dict_comprehension_invert.py`** — генерация словаря и инверсия ключей/значений с `pprint`.
  Запуск: `python3 dict_comprehension_invert.py`

- **`dict_merge_unpack.py`** — объединение словарей (распаковка, `update`, оператор `|`).
  Запуск: `python3 dict_merge_unpack.py`

- **`euler001_multiples_of_3_and_5.py`** — решение Project Euler #1 (сумма кратных 3 или 5).
  Запуск: `python3 euler001_multiples_of_3_and_5.py`

- **`eval_sum_expression.py`** — вычисление выражения `0+1+...+n-1` через `eval()`.
  Запуск: `python3 eval_sum_expression.py`

- **`extract_digits_to_int.py`** — извлечение целого числа из строки (удаление нецифровых символов).
  Запуск: `python3 extract_digits_to_int.py`

- **`file_write_read_demo.py`** — запись чисел в файл и чтение первой строки.
  Запуск: `python3 file_write_read_demo.py`

- **`find_char_positions.py`** — поиск всех позиций символа в строке (через `index` и `enumerate`).
  Запуск: `python3 find_char_positions.py`

- **`fizzbuzz_variants.py`** — четыре варианта реализации FizzBuzz.
  Запуск: `python3 fizzbuzz_variants.py`

- **`invert_dict.py`** — обмен ключей и значений в словаре.
  Запуск: `python3 invert_dict.py`

- **`largest_prime_factor.py`** — наибольший простой делитель числа (Project Euler #3).
  Запуск: `python3 largest_prime_factor.py`

- **`letter_count_and_positions.py`** — подсчёт количества и позиций заданной буквы в строке.
  Запуск: `python3 letter_count_and_positions.py`

- **`list_generation_methods.py`** — три способа создания списка из `range()`.
  Запуск: `python3 list_generation_methods.py`

- **`list_mutation_demo.py`** — изменение списка внутри функции (append, extend, срезы).
  Запуск: `python3 list_mutation_demo.py`

- **`palindrome_products.py`** — поиск палиндромов-произведений (брутфорс).
  Запуск: `python3 palindrome_products.py`

- **`palindrome_products_generate.py`** — оптимизированная генерация палиндромов-произведений.
  Запуск: `python3 palindrome_products_generate.py`

- **`prime_numbers_sieve.py`** — поиск простых чисел (наивный и решето Эратосфена).
  Запуск: `python3 prime_numbers_sieve.py`

- **`replace_single_asterisk.py`** — замена одиночных `*` на `!`, сохраняя `**`.
  Запуск: `python3 replace_single_asterisk.py`

- **`reverse_sequence.py`** — переворот кортежа/списка через срез.
  Запуск: `python3 reverse_sequence.py`

- **`reverse_string_generator.py`** — рекурсивный генератор для разворота строки.
  Запуск: `python3 reverse_string_generator.py`

- **`season_by_month.py`** — определение времени года по номеру месяца.
  Запуск: `python3 season_by_month.py`

- **`sum_of_cubes_digit_sum_divisible_by_7.py`** — сумма кубов чисел, сумма цифр которых кратна 7.
  Запуск: `python3 sum_of_cubes_digit_sum_divisible_by_7.py`

---

## Программы на C

- **`palindrome_index.c`** — проверка строки на палиндром (по индексам).
  Компиляция и запуск: `gcc -std=c11 palindrome_index.c -o palindrome_index && ./palindrome_index`

- **`palindrome_pointer.c`** — проверка строки на палиндром (через указатели).
  Компиляция и запуск: `gcc -std=c11 palindrome_pointer.c -o palindrome_pointer && ./palindrome_pointer`

- **`palindrome_manual.c`** — проверка строки на палиндром (посимвольное чтение).
  Компиляция и запуск: `gcc -std=c11 palindrome_manual.c -o palindrome_manual && ./palindrome_manual`

- **`rad_to_deg.c`** — перевод радиан в градусы с банковским округлением.
  Компиляция и запуск: `gcc -std=c11 rad_to_deg.c -lm -o rad_to_deg && ./rad_to_deg`

- **`remove_last_substr_strstr.c`** — удаление последнего вхождения подстроки (через `strstr`).
  Компиляция и запуск: `gcc -std=c11 remove_last_substr_strstr.c -o remove_last_substr_strstr && ./remove_last_substr_strstr`

- **`remove_last_substr_manual.c`** — удаление последнего вхождения подстроки (ручной поиск).
  Компиляция и запуск: `gcc -std=c11 remove_last_substr_manual.c -o remove_last_substr_manual && ./remove_last_substr_manual`

- **`groot.c`** — вывод фразы `"I'm Groot." (c) Groot`.
  Компиляция и запуск: `gcc -std=c11 groot.c -o groot && ./groot`

- **`binomial_coefficients.c`** — вывод биномиальных коэффициентов C(n, k) для k=0..n.
  Компиляция и запуск: `gcc -std=c11 binomial_coefficients.c -o binomial_coefficients && ./binomial_coefficients`

- **`max_before_minus_one.c`** — нахождение максимума в последовательности, оканчивающейся -1.
  Компиляция и запуск: `gcc -std=c11 max_before_minus_one.c -o max_before_minus_one && ./max_before_minus_one`

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

**Автор:** pavel-maru
**Репозиторий:** [https://github.com/pavel-maru/sandbox](https://github.com/pavel-maru/sandbox)
