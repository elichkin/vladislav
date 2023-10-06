from math import sqrt

def calc_truangle_square_gerone_calc(a, b, c):
    p = (a + b + c) / 2

    return sqrt(p * (p - a) * (p - b) * (p - c))