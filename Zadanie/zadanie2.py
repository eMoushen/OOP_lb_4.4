#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


class MyValidationError(Exception):
    def __init__(self, text):
        self.txt = text


def generate_matrix(rows, cols, start, end):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            value = randint(start, end)
            row.append(value)
        matrix.append(row)
    return matrix


if __name__ == "__main__":
    try:
        N = int(input('Строки: '))
        M = int(input('Столбцы: '))
        c = int(input('Начало диапазона целых чисел: '))
        d = int(input('Конец диапазона целых чисел: '))

        if (N <= 0) or (M <= 0):
            raise MyValidationError('Число должно быть положительным!')
        if d < c:
            raise MyValidationError('Начало диапазона не может быть больше конца!')

    except ValueError:
        print("Ошибка ввода. Введите целое число.")
    except MyValidationError as ve:
        print("Исключение:")
        print(ve)
    else:
        matrix = generate_matrix(N, M, c, d)
        for row in matrix:
            print()
            for value in row:
                print(value, end=" ")
        print()
