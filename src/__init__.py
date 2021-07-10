from fractions import Fraction
from math import floor


def cfrac_to_fraction(cfrac):
    ans = Fraction(cfrac.pop(0))
    if cfrac:
        ans = ans + (Fraction(1)/cfrac_to_fraction(cfrac))
    return ans


def fraction_to_cfrac(frac):
    ans = []
    while True:
        whole = floor(frac)
        ans.append(whole)
        frac = frac - whole
        if frac == 0:
            break
        frac = Fraction(1) / frac
    return ans
