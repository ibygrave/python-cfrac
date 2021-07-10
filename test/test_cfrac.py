from fractions import Fraction
import math

from cfrac import cfrac_to_fraction, fraction_to_cfrac
import pytest


@pytest.mark.parametrize(
    "cfrac,expected_frac",
    [
        ([1], Fraction("1")),
        ([1, 1], Fraction("2")),
        ([1, 2, 3], Fraction("10/7")),
    ],
)
def test_cfrac_to_fraction(cfrac, expected_frac):
    assert cfrac_to_fraction(cfrac) == expected_frac


@pytest.mark.parametrize(
    "frac,expected_cfrac",
    [
        (Fraction("5"), [5]),
        (Fraction("3/2"), [1, 2]),
        (Fraction("10/7"), [1, 2, 3]),
    ],
)
def test_fraction_to_cfrac(frac, expected_cfrac):
    assert fraction_to_cfrac(frac) == expected_cfrac


CPI = fraction_to_cfrac(Fraction(math.pi))


@pytest.mark.parametrize(
    "cfrac,limit_denom,expected_frac",
    [
        (CPI, 1, Fraction("3")),
        (CPI, 20, Fraction("22/7")),
        (CPI, 100, Fraction("22/7")),
        (CPI, 2000, Fraction("355/113")),
        (CPI, 10000, Fraction("355/113")),
    ],
)
def test_cfrac_to_fraction_limit_denom(cfrac, limit_denom, expected_frac):
    assert cfrac_to_fraction(cfrac, limit_denom=limit_denom) == expected_frac
