#!/usr/bin/python3
from decimal import Decimal as Dec, getcontext as gtc


# Generate pi to nth digit
# Chudnovsky algorihtm to find pi to n-th digit
# from https://en.wikipedia.org/wiki/Chudnovsky_algorithm
def pi_calc(n):
    gtc().prec = n + 2
    C = 426880 * Dec(10005).sqrt()
    K = 6.0
    M = 1.0
    X = 1
    L = 13591409
    S = L
    for i in range(1, n):
        M = M * (K ** 3 - 16 * K) / ((i + 1) ** 3)
        L += 545140134
        X *= -262537412640768000
        S += Dec(M * L) / X
    pi = C / S
    print(pi)


if __name__ == "__main__":
    pi_calc(4096)

