/**
 * @file palindrome_index.c
 * @brief Проверка, является ли строка палиндромом (с использованием индексов).
 *
 * Программа считывает строку из стандартного ввода, удаляет завершающий символ
 * новой строки, затем проверяет, читается ли строка одинаково слева направо
 * и справа налево. Выводит "yes" или "no".
 *
 * Алгоритм: сравнивает символы с обоих концов, двигаясь к центру.
 * Регистр и пробелы учитываются (можно легко изменить, добавив приведение к нижнему
 * регистру или игнорирование пробелов).
 *
 * @author pavel_maru
 * @date 2026-08-19
 * @version 1.0
 *
 * @compile gcc -std=c11 -Wall -Wextra -O2 palindrome_index.c -o palindrome_index
 * @run ./palindrome_index
 */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LEN 100

/**
 * @brief Проверяет, является ли строка палиндромом.
 *
 * @param str Проверяемая строка (должна быть завершена '\0').
 * @return true, если строка палиндром, иначе false.
 */
bool is_palindrome(const char *str) {
    size_t len = strlen(str);
    if (len == 0) return true;  // пустая строка считается палиндромом

    for (size_t i = 0; i < len / 2; i++) {
        if (str[i] != str[len - 1 - i]) {
            return false;
        }
    }
    return true;
}

/**
 * @brief Безопасное чтение строки с удалением завершающего \n.
 *
 * @param buffer Указатель на буфер.
 * @param size Размер буфера.
 * @return true при успехе, false при ошибке.
 */
bool safe_read_line(char *buffer, size_t size) {
    if (fgets(buffer, size, stdin) == NULL) {
        return false;
    }
    // Удаляем символ новой строки, если он есть
    buffer[strcspn(buffer, "\n")] = '\0';
    return true;
}

int main(void) {
    char str[MAX_LEN];

    printf("Введите строку: ");
    if (!safe_read_line(str, sizeof(str))) {
        fprintf(stderr, "Ошибка чтения строки.\n");
        return 1;
    }

    if (is_palindrome(str)) {
        printf("yes\n");
    } else {
        printf("no\n");
    }

    return 0;
}
