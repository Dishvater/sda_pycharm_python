#!/usr/bin/env python
# -*- coding: utf-8 -*-


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)


if __name__ == '__main__':
    value = 6
    result = factorial(value)
    print(f'Factorial of {value} is {result}')
