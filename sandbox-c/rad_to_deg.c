/**
 * @file rad_to_deg.c
 * @brief Конвертация радианной меры в градусы с банковским округлением.
 *
 * Программа считывает значение в радианах (тип double), проверяет его на
 * корректность (конечное число, не NaN, не бесконечность), переводит в градусы
 * и округляет результат до целого числа по правилам банковского округления
 * (half-to-even). Выводит целое число градусов.
 *
 * Используется стандартная библиотека C и округление через nearbyint с установкой
 * режима FE_TONEAREST (по умолчанию). Обрабатываются ошибки ввода и нечисловые
 * значения.
 *
 * @author pavel_maru
 * @date 2026-08-19
 * @version 1.0
 *
 * @compile gcc -std=c11 -Wall -Wextra -O2 rad_to_deg.c -lm -o rad_to_deg
 * @run ./rad_to_deg
 */

#include <fenv.h>      // fesetround, FE_TONEAREST
#include <math.h>      // nearbyint, isfinite, M_PI
#include <stdio.h>     // printf, scanf
#include <stdlib.h>    // exit, EXIT_SUCCESS, EXIT_FAILURE

#ifndef M_PI
    #define M_PI 3.14159265358979323846
#endif

/**
 * @brief Банковское округление (half-to-even) для double.
 *
 * Использует nearbyint(), которая округляет согласно текущему режиму округления.
 * Явно устанавливает FE_TONEAREST (округление до ближайшего целого, при .5 – к чётному).
 *
 * @param x Число с плавающей точкой.
 * @return Округлённое значение в виде long.
 */
long bank_round(double x) {
    fesetround(FE_TONEAREST);
    return (long)nearbyint(x);
}

/**
 * @brief Проверяет, является ли введённая строка корректным числом с плавающей точкой.
 *
 * Считывает double из stdin. В случае ошибки выводит сообщение и завершает программу.
 *
 * @param[out] value Указатель на переменную для сохранения введённого значения.
 * @return EXIT_SUCCESS при успехе, иначе EXIT_FAILURE.
 */
int read_radians(double *value) {
    int result = scanf("%lf", value);
    if (result != 1) {
        fprintf(stderr, "Ошибка: введено не число.\n");
        return EXIT_FAILURE;
    }
    // Проверка на конечность (не NaN и не бесконечность)
    if (!isfinite(*value)) {
        fprintf(stderr, "Ошибка: введено некорректное значение (бесконечность или NaN).\n");
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}

/**
 * @brief Преобразует радианы в градусы.
 *
 * @param rad Значение в радианах.
 * @return Значение в градусах (double).
 */
double radians_to_degrees(double rad) {
    return rad * 180.0 / M_PI;
}

/**
 * @brief Главная функция программы.
 *
 * Считывает радианы, преобразует в градусы, округляет и выводит результат.
 *
 * @return 0 при успехе, 1 при ошибке.
 */
int main(void) {
    double radians;

    printf("Введите значение в радианах: ");

    if (read_radians(&radians) != EXIT_SUCCESS) {
        return EXIT_FAILURE;
    }

    double degrees = radians_to_degrees(radians);
    long rounded = bank_round(degrees);

    printf("Результат: %ld градусов\n", rounded);

    return EXIT_SUCCESS;
}
