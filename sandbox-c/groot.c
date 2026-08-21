/**
 * @file groot.c
 * @brief Программа выводит фразу Groot с кавычками.
 *
 * @compile gcc -std=c11 -Wall -Wextra -O2 groot.c -o groot
 * @run ./groot
 */

#include <stdio.h>

int main(void) {
    // Экранируем кавычки: \" для вывода символа "
    printf("\"I'm Groot.\" (c) Groot\n");
    return 0;
}
