import math


def expoential(val):
    x = math.exp((val))
    y = math.exp(-(val))
    sigma = x/(x+1)
    hyberbolic = (x-y)/(x+y)
    return sigma, hyberbolic


print(expoential(1))
