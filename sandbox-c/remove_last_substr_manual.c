/**
 * @file remove_last_substr_manual.c
 * @brief Удаление последнего вхождения подстроки из строки (ручной поиск с конца).
 *
 * Программа считывает две строки (исходную и подстроку) из стандартного ввода,
 * находит последнее вхождение подстроки в исходной строке и удаляет его,
 * сдвигая остаток влево. Если подстрока не найдена или пуста, исходная строка
 * выводится без изменений.
 *
 * Алгоритм: вычисляет последнюю возможную позицию для подстроки (len_str - len_sub),
 * затем идёт от конца к началу и сравнивает фрагменты с помощью strncmp.
 * Как только совпадение найдено, удаляет его сдвигом.
 *
 * Преимущество: поиск с конца может быть быстрее, если подстрока встречается редко.
 *
 * @author pavel_maru
 * @date 2026-08-19
 * @version 1.0
 *
 * @compile gcc -std=c11 -Wall -Wextra -O2 remove_last_substr_manual.c -o remove_last_substr_manual
 * @run ./remove_last_substr_manual
 */

#include <stdio.h>
#include <string.h>

/**
 * @brief Находит указатель на последнее вхождение подстроки в строке.
 *
 * @param str Исходная строка (const).
 * @param substr Искомая подстрока.
 * @return Указатель на начало последнего вхождения или NULL, если не найдено.
 */
const char *last_occurrence(const char *str, const char *substr) {
    size_t len_str = strlen(str);
    size_t len_sub = strlen(substr);

    if (len_sub == 0 || len_sub > len_str) return NULL;

    const char *start = str;
    const char *end = str + len_str - len_sub;  // последняя возможная позиция

    // Идём с конца к началу
    for (const char *p = end; p >= start; --p) {
        if (strncmp(p, substr, len_sub) == 0) {
            return p;
        }
        if (p == start) break;  // чтобы не выйти за пределы
    }
    return NULL;
}

/**
 * @brief Удаляет последнее вхождение подстроки из строки (in-place).
 *
 * @param str Указатель на изменяемую строку.
 * @param substr Подстрока для удаления.
 * @return 0 при успехе, -1 если подстрока пуста или не найдена.
 */
int remove_last_occurrence(char *str, const char *substr) {
    if (str == NULL || substr == NULL) return -1;
    size_t sub_len = strlen(substr);
    if (sub_len == 0) return -1;

    const char *pos = last_occurrence(str, substr);
    if (pos == NULL) return -1;

    // pos указывает на начало подстроки внутри str
    char *start = (char *)pos;
    memmove(start, start + sub_len, strlen(start + sub_len) + 1);
    return 0;
}

/**
 * @brief Безопасное чтение строки с удалением завершающего \n.
 */
char *safe_fgets(char *buffer, size_t size) {
    if (fgets(buffer, size, stdin) == NULL) return NULL;
    buffer[strcspn(buffer, "\n")] = '\0';
    return buffer;
}

int main(void) {
    char str[1024];
    char substr[1024];

    printf("Введите исходную строку: ");
    if (safe_fgets(str, sizeof(str)) == NULL) {
        fprintf(stderr, "Ошибка чтения исходной строки.\n");
        return 1;
    }

    printf("Введите подстроку для удаления: ");
    if (safe_fgets(substr, sizeof(substr)) == NULL) {
        fprintf(stderr, "Ошибка чтения подстроки.\n");
        return 1;
    }

    int status = remove_last_occurrence(str, substr);
    if (status == 0) {
        printf("Результат: %s\n", str);
    } else {
        printf("Подстрока не найдена или пуста. Строка без изменений: %s\n", str);
    }

    return 0;
}
