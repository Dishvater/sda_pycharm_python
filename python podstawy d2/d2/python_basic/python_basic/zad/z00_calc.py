#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    end = False
    while not end:
        number_1 = float(input('Input 1st number: '))
        operation = input('Input math operation sign [+,-,*,/,%]: ')
        number_2 = float(input('Input 2nd number: '))

        if operation == "+":
            result = number_1 + number_2
        elif operation == "-":
            result = number_1 - number_2
        elif operation == "*":
            result = number_1 * number_2
        elif operation == "/":
            result = number_1 / number_2
        elif operation == "%":
            result = number_1 % number_2
        else:
            print("Wrong operation")
            break

        print(f"Result: {result}")
        print("Next operation? Input y or n")

        next_choice = input()
        if next_choice == "n":
            end = True
        elif next_choice != "y":
            print("Wrong choice")
            break


if __name__ == "__main__":
    main()
