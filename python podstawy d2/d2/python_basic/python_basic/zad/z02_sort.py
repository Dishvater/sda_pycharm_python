#!/usr/bin/env python
# -*- coding: utf-8 -*-

TEST = [
    'Bardzo lubię pomarańcza i ogórki',
    'Kiedy litery nie są po kolei'
]


def sort_words(sentence: str):
    words = sentence.split()
    return sorted(words)


if __name__ == '__main__':
    for test in TEST:
        result = sort_words(test)
        print(result)
        for index, word in enumerate(result):
            print(word)
            if index == 2:
                break

