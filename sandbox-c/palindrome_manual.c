/**
 * @file palindrome_my.c
 * @brief Проверка строки на палиндром (посимвольное чтение, без strlen).
 *
 * Программа читает символы из стандартного ввода до символа новой строки,
 * сохраняет их в массив, а затем проверяет, является ли введённая строка
 * палиндромом. Используется только базовая арифметика указателей и индексов.
 *
 * Этот файл демонстрирует, как можно обойтись без стандартных строковых функций
 * (strlen, strcmp и т.д.) и выполнить проверку "вручную".
 *
 * @author pavel_maru
 * @date 2026-08-19
 * @version 1.0
 *
 * @compile gcc -std=c11 -Wall -Wextra -O2 palindrome_my.c -o palindrome_my
 * @run ./palindrome_my
 */

#include <stdio.h>
#include <stdbool.h>

#define MAX_LEN 100

/**
 * @brief Читает строку из stdin до '\n' и сохраняет в массив.
 *
 * @param buffer Массив для сохранения символов.
 * @param max_size Максимальное количество символов (включая завершающий '\0').
 * @return Количество прочитанных символов (без учёта '\0'), или -1 при ошибке.
 */
int read_line(char *buffer, int max_size) {
    int count = 0;
    int ch;

    while (count < max_size - 1) {
        ch = getchar();
        if (ch == EOF) {
            return -1;            // конец файла или ошибка
        }
        if (ch == '\n') {
            break;                // конец строки
        }
        buffer[count++] = (char)ch;
    }
    buffer[count] = '\0';         // завершающий нуль
    return count;
}

/**
 * @brief Проверяет, является ли строка палиндромом.
 *
 * @param str Строка, завершающаяся '\0'.
 * @param len Длина строки (без '\0').
 * @return true, если палиндром, иначе false.
 */
bool is_palindrome(const char *str, int len) {
    if (len <= 1) {
        return true;   // пустая строка или один символ — палиндром
    }
    int left = 0;
    int right = len - 1;
    while (left < right) {
        if (str[left] != str[right]) {
            return false;
        }
        left++;
        right--;
    }
    return true;
}

int main(void) {
    char buffer[MAX_LEN];
    int len;

    printf("Введите строку: ");
    len = read_line(buffer, MAX_LEN);

    if (len < 0) {
        fprintf(stderr, "Ошибка чтения строки.\n");
        return 1;
    }

    if (is_palindrome(buffer, len)) {
        printf("yes\n");
    } else {
        printf("no\n");
    }

    return 0;
}
