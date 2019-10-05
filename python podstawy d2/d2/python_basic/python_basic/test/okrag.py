from math import pi


def circle_area(r: float):
    return pi * r ** 2


def circumference(r: float):
    return 2 * pi * r


if __name__ == '__main__':
    print(circle_area(3))
