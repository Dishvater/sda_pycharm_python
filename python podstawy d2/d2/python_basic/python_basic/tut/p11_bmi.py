def calculate_bmi(weight: float, height: float) -> str:
    bmi = weight / height ** 2
    if bmi < 18.5:
        result = 'underweight'
    elif bmi > 25:
        result = 'overweight'
    else:
        result = 'normal'
    return result


if __name__ == '__main__':
    user_weight = float(input('Weight in [kg]: '))
    user_height = float(input('Height in [m]: '))
    user_result = calculate_bmi(weight=user_weight, height=user_height)
    print(f'Your BMI says {user_result}')
