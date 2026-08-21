/**
 * @file binomial_coefficients.c
 * @brief Вывод строки биномиальных коэффициентов C(n, k) для k = 0..n.
 *
 * Программа считывает целое неотрицательное число n из stdin,
 * вычисляет последовательные коэффициенты по рекуррентной формуле
 * C(n, k+1) = C(n, k) * (n - k) / (k + 1) и выводит их через пробел.
 *
 * @compile gcc -std=c11 -Wall -Wextra -O2 binomial_coefficients.c -o binomial_coefficients
 * @run ./binomial_coefficients
 */

#include <stdio.h>

int main(void) {
    unsigned long long n;   // используем беззнаковый тип для неотрицательных n

    printf("Введите неотрицательное целое число n: ");
    if (scanf("%llu", &n) != 1) {
        fprintf(stderr, "Ошибка ввода: ожидалось целое неотрицательное число.\n");
        return 1;
    }

    // Первый коэффициент C(n, 0) = 1
    unsigned long long current = 1;
    printf("%llu", current);   // выводим первый без пробела

    // Вычисляем остальные коэффициенты
    for (unsigned long long k = 1; k <= n; ++k) {
        // C(n, k) = C(n, k-1) * (n - k + 1) / k
        // Чтобы избежать переполнения, сначала умножаем, потом делим.
        // Для очень больших n всё равно может произойти переполнение,
        // но в учебных целях это допустимо.
        current = current * (n - k + 1) / k;
        printf(" %llu", current);
    }

    printf("\n");
    return 0;
}
