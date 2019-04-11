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
    if (iq < 0):
        quit (84)
    i = 0
    result = 0.0

    while (i < iq):
        result += formule_205(i, mu, sigma)
        i += 1
    return result * 100

def mode_3(mu, sigma, IQstr1, IQstr2):
    prop1 = mode_2(mu, sigma, IQstr1)
    prop2 = mode_2(mu, sigma, IQstr2)

    result = prop2 - prop1

    print("%.1f" % (result), "% " ,"of people have an IQ between ", IQstr1, " and ", IQstr2, sep='')

    return