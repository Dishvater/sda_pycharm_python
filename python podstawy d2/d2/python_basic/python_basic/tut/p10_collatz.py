#!/usr/bin/env python
# -*- coding: utf-8 -*-


def collatz(number):
    print(number)
    if number == 1:
        return
    elif number % 2:
        return collatz(number * 3 + 1)
    else:
        return collatz(number // 2)


if __name__ == '__main__':
    user_number = int(input('Input a number: '))
    print(f'Collatz sequence for number {user_number} is: ')
    collatz(user_number)
