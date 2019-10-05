#!/usr/bin/env python
# -*- coding: utf-8 -*-

suspect_1 = 'GAGCCTACTAACGGGAT'
suspect_2 = 'GAGCCTACTAACAAAAT'
child = 'CATCGTAATGACGGCCT'


def hamming(strand_a, strand_b):
    result = 0
    zipped_strands = zip(strand_a, strand_b)
    for item_a, item_b in zipped_strands:
        if item_a != item_b:
            result += 1
    return result


if __name__ == '__main__':
    print(f'Suspect #1: {suspect_1}')
    print(f'Suspect #2: {suspect_2}')
    print(f'Child: {child}')
    distance_1 = hamming(suspect_1, child)
    distance_2 = hamming(suspect_2, child)
    if distance_1 < distance_2:
        print('Suspect #1 is a father')
    else:
        print('Suspect #2 is a father')
