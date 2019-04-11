#/bin/python3

from math import pi, sqrt, exp
import time

def formule_205(i, mu, sigma):
    tmp = exp(-((i - mu) * (i - mu) / (2 * sigma * sigma)))
    result = 1 / (sigma * sqrt(2 * pi)) * tmp
    return result

def mode_1(mu, sigma):
    i = 0
    result = 0.0

    while (i <= 200):
        result = formule_205(i, mu, sigma)
        print(i, "%.5f" % result)
        i += 1
    return

def mode_2(mu, sigma, IQstr):
    try:
        iq = int(IQstr)
    except:
        quit(84)
    
    i = 0
    result = 0.0

    while (i < iq):
        result += formule_205(i, mu, sigma)
        i += 1
    print(result * 100)
    return

def mode_3(mu, sigma, IQstr1, IQstr2):
    return