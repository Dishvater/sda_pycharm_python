#!/usr/bin/env python
# -*- coding: utf-8 -*-


def count_down(number):
    while number:
        number -= 1
        if number % 2:
            print(number)
            continue
    print('Now we know while loop!')


if __name__ == '__main__':
    count_down(10)
