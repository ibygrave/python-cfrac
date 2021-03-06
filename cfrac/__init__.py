"""Continued Fractions"""
from fractions import Fraction
from math import floor


def cfrac_to_fraction(cfrac, limit_denom=None):
    """Convert a continued fraction to a Fraction"""
    terms = cfrac[:]
    assert limit_denom is None or limit_denom >= 1
    ans = Fraction(terms.pop(0))
    if terms:
        ans = ans + (Fraction(1) / cfrac_to_fraction(terms))
    if (
        (limit_denom is not None)
        and (ans.denominator > limit_denom)
        and (len(cfrac) > 1)
    ):
        return cfrac_to_fraction(cfrac[:-1], limit_denom)
    return ans


def fraction_to_cfrac(frac):
    """Convert a Fraction to a continued fraction"""
    ans = []
    while True:
        whole = floor(frac)
        ans.append(whole)
        frac = frac - whole
        if frac == 0:
            break
        frac = Fraction(1) / frac
    return ans
