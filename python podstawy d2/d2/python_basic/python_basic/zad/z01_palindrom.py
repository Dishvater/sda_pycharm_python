#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_palindrom(napis):
    n = len(napis)
    for i in range(len(napis)//2):
        if napis[i] != napis[n-i-1]:
            return False
    return True


def is_palindrom_2(napis):
    return napis == napis[::-1]


if __name__ == '__main__':
    while True:
        my_word = input('Input a word: ').strip()
        answer = 'is' if is_palindrom_2(my_word) else 'is not'
        print(f'Word {my_word} {answer} an palindrom\n')
        shall_continue = input('Do you want to continue (y/n)?: ')
        if shall_continue != 'y':
            break
