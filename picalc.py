"""
Generate pi to a given number of digits

original code: https://docs.python.org/3/library/decimal.html#recipes
"""
#!/usr/bin/env python3
# cython: language_level=3
from decimal import Decimal as D, getcontext as gc
from sys import argv


# function to parallelize
def adder(x):
    return (x[0] + x[1], x[0] + x[2])


def pi(precision=42):
    """ Compute Pi to the current precision. """
    gc().prec = precision
    gc().prec += 2  # extra digits for intermediate steps

    three = D(3)  # substitute "three=3.0" for regular floats
    end, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24

    # main calculation process
    while s != end:
        (end, _), (n, na), (d, da) = map(
            adder, ((0, s, 0), (na, n, 8), (da, d, 32))
        )
        t = (t * n) / d
        s += t

    gc().prec -= 2  # drop the previously added digits for accuracy
    return +s  # unary plus applies the new precision


if __name__ == "__main__":
    print(pi(int(argv[1]) if len(argv) > 1 else 42))

# Generate pi to nth digit
# Chudnovsky algorihtm to find pi to n-th digit
# from https://en.wikipedia.org/wiki/Chudnovsky_algorithm
#def pi_calc(n):
#    gtc().prec = n + 2
#    C = 426880 * Dec(10005).sqrt()
#    K = 6.0
#    M = 1.0
#    X = 1
#    L = 13591409
#    S = L
#    for i in range(1, n):
#        M *= (K ** 3 - 16 * K) / ((i + 1) ** 3)
#        L += 545140134
#        X *= -262537412640768000
#        S += Dec(M * L) / X
#    pi = C / S
#    print(pi)

