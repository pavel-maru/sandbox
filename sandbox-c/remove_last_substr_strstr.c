/**
 * @file remove_last_substr_strstr.c
 * @brief Удаление последнего вхождения подстроки из строки (с использованием strstr).
 *
 * Программа считывает две строки (исходную и подстроку) из стандартного ввода,
 * находит последнее вхождение подстроки в исходной строке и удаляет его,
 * сдвигая остаток влево. Если подстрока не найдена или пуста, исходная строка
 * выводится без изменений.
 *
 * Алгоритм: последовательно вызывает strstr, начиная с каждого следующего символа,
 * запоминая последнее найденное вхождение. После цикла удаляет найденную подстроку
 * с помощью memmove.
 *
 * Ограничения: максимальная длина строки задана макросом MAX_LEN (4096).
 * При вводе строк длиннее буфера они будут обрезаны.
 *
 * @author pavel_maru
 * @date 2026-08-19
 * @version 1.0
 *
 * @compile gcc -std=c11 -Wall -Wextra -O2 remove_last_substr_strstr.c -o remove_last_substr_strstr
 * @run ./remove_last_substr_strstr
 */

#include <stdio.h>
#include <string.h>

#define MAX_LEN 4096

/**
 * @brief Удаляет последнее вхождение подстроки из строки (in-place).
 *
 * @param str Указатель на изменяемую строку (должна иметь достаточный размер).
 * @param substr Подстрока для удаления.
 * @return 0 при успехе, -1 если подстрока пуста или не найдена.
 */
int remove_last_occurrence(char *str, const char *substr) {
    if (str == NULL || substr == NULL) return -1;
    size_t sub_len = strlen(substr);
    if (sub_len == 0) return -1;  // пустая подстрока — ничего не делаем

    char *last = NULL;
    char *cur = strstr(str, substr);
    while (cur != NULL) {
        last = cur;
        cur = strstr(cur + 1, substr);  // поиск со следующего символа (перекрытия допустимы)
    }

    if (last == NULL) return -1;  // не найдено

    // Удаляем подстроку сдвигом остатка
    memmove(last, last + sub_len, strlen(last + sub_len) + 1);
    return 0;
}

/**
 * @brief Безопасное чтение строки с удалением завершающего \n.
 *
 * @param buffer Указатель на буфер.
 * @param size Размер буфера.
 * @return Указатель на buffer при успехе, NULL при ошибке.
 */
char *safe_fgets(char *buffer, size_t size) {
    if (fgets(buffer, size, stdin) == NULL) return NULL;
    buffer[strcspn(buffer, "\n")] = '\0';  // убираем \n, если он есть
    return buffer;
}

int main(void) {
    char str[MAX_LEN];
    char substr[MAX_LEN];

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
