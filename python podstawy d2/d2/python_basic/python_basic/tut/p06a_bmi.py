#!/usr/bin/env python
# -*- coding: utf-8 -*-


def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        result = 'underweight'
    elif bmi > 25:
        result = 'overweight'
    else:
        result = 'normal'
    return result, bmi


if __name__ == '__main__':
    user_weight = float(input('Weight in [kg]: '))
    user_height = float(input('Height in [m]: '))
    user_result, user_bmi = calculate_bmi(user_weight, user_height)
    print(f'Your BMI: {user_bmi:.2f} says {user_result}')
    print('Your BMI: {:.2f} says {}'.format(user_bmi, user_result))

