#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_leap_year(year: str):
    if not int(year) % 4 and not year.endswith('00'):
        return True
    elif not int(year) % 400 and year.endswith('00'):
        return True
    else:
        return False


def is_leap_year_2(year: str):
    if year.endswith('00'):
        if not int(year) % 400:
            return True
    else:
        if not int(year) % 4:
            return True
    return False


if __name__ == '__main__':
    while True:
        my_year = input('Input a year: ').strip()
        answer = 'is' if is_leap_year_2(my_year) else 'is not'
        print(f'Year {my_year} {answer} a leap year\n')
        shall_continue = input('Do you want to continue (y/n)?: ')
        if shall_continue != 'y':
            break
