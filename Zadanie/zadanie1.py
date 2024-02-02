#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass(frozen=True)
class Container:
    x: str


@dataclass
class Sum:
    def __init__(self, a: Container, b: Container):
        """
        Если оба x - это числа, то суммируем их, иначе конкатенируем строки
        """
        try:
            x, y = int(a.x), int(b.x)
        except ValueError:
            x, y = a.x, b.x

        self.res = x + y

    def __str__(self):
        return str(self.res)


if __name__ == '__main__':
    a = Container(x=input("Первое значение: "))
    b = Container(x=input("Второе значение: "))

    print(Sum(a, b))
