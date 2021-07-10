from fractions import Fraction

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
        (Fraction("1146408/364913"), [3, 7, 15, 1, 292, 1, 1, 1, 3])
    ],
)
def test_fraction_to_cfrac(frac, expected_cfrac):
    assert fraction_to_cfrac(frac) == expected_cfrac


CPI = fraction_to_cfrac(Fraction("1146408/364913"))


@pytest.mark.parametrize(
    "cfrac,limit_denom,expected_frac",
    [
        (CPI, 1, Fraction("3")),
        (CPI, 6, Fraction("3")),
        (CPI, 7, Fraction("22/7")),
        (CPI, 105, Fraction("22/7")),
        (CPI, 106, Fraction("333/106")),
        (CPI, 112, Fraction("333/106")),
        (CPI, 113, Fraction("355/113")),
        (CPI, 33101, Fraction("355/113")),
        (CPI, 33102, Fraction("103993/33102")),
        (CPI, 33214, Fraction("103993/33102")),
        (CPI, 33215, Fraction("104348/33215")),
    ],
)
def test_cfrac_to_fraction_limit_denom(cfrac, limit_denom, expected_frac):
    assert cfrac_to_fraction(cfrac, limit_denom=limit_denom) == expected_frac
