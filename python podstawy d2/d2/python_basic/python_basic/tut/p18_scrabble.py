#!/usr/bin/env python
# -*- coding: utf-8 -*-
scores = {
    "a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4, "g": 2, "h": 4,
    "i": 1, "j": 8, "k": 5, "l": 1, "m": 3, "n": 1, "o": 1, "p": 3,
    "q": 10, "r": 1, "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
    "y": 4, "z": 10
}


def scrabble_score(word):
    # total_score = 0
    # for letter in word.lower():
    #     total_score += scores[letter]

    total_score = sum([scores[litera] for litera in word.lower()])
    return total_score


if __name__ == '__main__':
    while True:
        my_word = input('Input a word: ').strip()
        score = scrabble_score(my_word)
        print(f'Word {my_word} is worth {score} points\n')
        shall_continue = input('Do you want to continue (y/n)?: ')
        if shall_continue != 'y':
            break
