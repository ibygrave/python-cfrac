from fractions import Fraction

from cfrac import cfrac_to_fraction
import pytest


@pytest.mark.parametrize("cfrac,expected_frac", [
    ([1], Fraction("1")),
    ([1,1], Fraction("2")),
    ([1,2,3], Fraction("10/7")),
    ])
def test_cfrac_to_frac(cfrac, expected_frac):
    assert cfrac_to_fraction(cfrac) == expected_frac
