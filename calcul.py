#/bin/python3

from math import pi, sqrt, exp
import time

def mode_1(mu, sigma):
    i = 0
    tmp = 0.0
    result = 0.0

    while (i <= 200):
        tmp = exp(-((i - mu) * (i - mu) / (2 * sigma * sigma)))
        result = 1 / (sigma * sqrt(2 * pi)) * tmp
        print(i, "%.5f" % result)
        i += 1
    return

def mode_2(mu, sigma, IQstr):
    return

def mode_3(mu, sigma, IQstr1, IQstr2):
    return