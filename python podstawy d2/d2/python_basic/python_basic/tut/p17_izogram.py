#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_isogram(word):
    letters = set()
    for letter in word.lower():
        if letter in letters:
            return False
        letters.add(letter)
    return True


if __name__ == '__main__':
    while True:
        my_word = input('Input a word: ').strip()
        answer = 'is' if is_isogram(my_word) else 'is not'
        print(f'Word {my_word} {answer} an isogram\n')
        shall_continue = input('Do you want to continue (y/n)?: ')
        if shall_continue != 'y':
            break
