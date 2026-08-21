/**
 * @file max_before_minus_one.c
 * @brief Нахождение максимума в последовательности целых чисел, завершающейся -1.
 *
 * Программа читает числа из stdin, пока не встретит -1.
 * Затем выводит максимальное из введённых чисел.
 * Если последовательность пуста (первое число -1), выводится сообщение об ошибке.
 *
 * @compile gcc -std=c11 -Wall -Wextra -O2 max_before_minus_one.c -o max_before_minus_one
 * @run ./max_before_minus_one
 */

#include <stdio.h>
#include <limits.h>

int main(void) {
    int value;
    int max_value;
    int has_value = 0;   // флаг, было ли введено хотя бы одно число (не -1)

    printf("Введите целые числа, для завершения введите -1:\n");

    // Считываем первое число
    if (scanf("%d", &value) != 1) {
        fprintf(stderr, "Ошибка ввода.\n");
        return 1;
    }

    // Если сразу -1 — массив пуст
    if (value == -1) {
        fprintf(stderr, "Массив пуст (сразу введён -1).\n");
        return 1;
    }

    // Инициализируем максимум первым числом
    max_value = value;
    has_value = 1;

    // Читаем остальные числа до -1
    while (scanf("%d", &value) == 1 && value != -1) {
        if (value > max_value) {
            max_value = value;
        }
        has_value = 1;
    }

    // Проверяем, что завершились не из-за ошибки, а из-за -1
    // (если вышли из цикла из-за конца файла, это не ошибка, но поведение не определено)
    // Можно дополнительно проверить, что последний прочитанный int был -1,
    // но в данном цикле мы выходим только при value == -1, значит так и есть.

    if (has_value) {
        printf("Максимальное значение: %d\n", max_value);
    } else {
        fprintf(stderr, "Не было введено ни одного числа (кроме -1).\n");
        return 1;
    }

    return 0;
}
