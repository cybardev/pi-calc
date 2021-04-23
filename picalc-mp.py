"""
Generate pi to a given number of digits

original code: https://docs.python.org/3/library/decimal.html#recipes
"""
#!/usr/bin/env python3
# cython: language_level=3
from decimal import Decimal as D, getcontext as gc
import multiprocessing as mp
from sys import argv


# function to parallelize
def adder(*x):
    return (x[0] + x[1], x[0] + x[2])


def pi(precision=42):
    """ Compute Pi to the current precision. """
    gc().prec = precision
    gc().prec += 2  # extra digits for intermediate steps

    three = D(3)  # substitute "three=3.0" for regular floats
    end, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24

    # main calculation process
    with mp.Pool(3) as p:
        while s != end:
            (end, _) = p.apply_async(adder, (0, s, 0)).get()
            (n, na) = p.apply_async(adder, (na, n, 8)).get()
            (d, da) = p.apply_async(adder, (da, d, 32)).get()
            t = (t * n) / d
            s += t

    gc().prec -= 2  # drop the previously added digits for accuracy
    return +s  # unary plus applies the new precision


if __name__ == "__main__":
    print(pi(int(argv[1]) if len(argv) > 1 else 42))
