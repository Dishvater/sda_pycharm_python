#!/usr/bin/env python
# -*- coding: utf-8 -*-

a_list = [1, 2, 3, 4]
b_list = [1, 2, 3, 4, 5, 6]


def sum_list(*args) -> float:
    return sum(*args)


def my_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result


if __name__ == '__main__':
    result = sum_list(a_list)
    print(f'Sum of {a_list} is: {result}')
    result = sum_list(b_list)
    print(f'Sum of {b_list} is: {result}')
    print(my_sum(1, 2, 3, 4, 5))
