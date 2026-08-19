/**
 * @file palindrome_pointer.c
 * @brief Проверка, является ли строка палиндромом (с использованием указателей).
 *
 * Программа считывает строку из стандартного ввода, удаляет завершающий символ
 * новой строки, затем проверяет, читается ли строка одинаково слева направо
 * и справа налево. Использует два указателя: один на начало, другой на конец.
 *
 * Алгоритм: указатель left идёт с начала, right с конца, сравниваются символы,
 * указатели сдвигаются навстречу друг другу.
 *
 * @author pavel_maru
 * @date 2026-08-19
 * @version 1.0
 *
 * @compile gcc -std=c11 -Wall -Wextra -O2 palindrome_pointer.c -o palindrome_pointer
 * @run ./palindrome_pointer
 */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

#define MAX_LEN 100

/**
 * @brief Проверяет, является ли строка палиндромом (используя указатели).
 *
 * @param str Проверяемая строка.
 * @return true, если палиндром, иначе false.
 */
bool is_palindrome(const char *str) {
    const char *left = str;
    const char *right = str + strlen(str) - 1;

    // Пустая строка или строка из одного символа — палиндром
    if (right < left) return true;

    while (left < right) {
        if (*left != *right) {
            return false;
        }
        left++;
        right--;
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
