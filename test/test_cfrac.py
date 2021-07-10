from fractions import Fraction

from cfrac import cfrac_to_fraction, fraction_to_cfrac
import pytest


@pytest.mark.parametrize("cfrac,expected_frac", [
    ([1], Fraction("1")),
    ([1,1], Fraction("2")),
    ([1,2,3], Fraction("10/7")),
    ])
def test_cfrac_to_fraction(cfrac, expected_frac):
    assert cfrac_to_fraction(cfrac) == expected_frac


@pytest.mark.parametrize("frac,expected_cfrac", [
    (Fraction("5"), [5]),
    (Fraction("3/2"), [1,2]),
    (Fraction("10/7"), [1,2,3]),
    ])
def test_fraction_to_cfrac(frac, expected_cfrac):
    assert fraction_to_cfrac(frac) == expected_cfrac
