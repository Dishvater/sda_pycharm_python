#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randrange


if __name__ == '__main__':
    random_number = randrange(10)
    print(random_number)
    while True:
        guess = input('Input a number[1-10]: ').strip()
        answer = random_number == int(guess)
        if answer:
            print(f'Number {guess} is a good guess\n')
            break
        else:
            print(f'Try again\n')
        shall_continue = input('Do you want to continue (y/n)?: ')
        if shall_continue != 'y':
            break
