#!/usr/bin/env python
# -*- coding: utf-8 -*-


def count_down(number):
    while number:
        print(number)
        number -= 1
        if number == 5:
            print('Aborted!')
            break
    print('Now we know while loop!')


if __name__ == '__main__':
    count_down(10)
