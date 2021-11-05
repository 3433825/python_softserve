import pytest
from calculator import calc

@pytest.mark.parametrize("example,expected", [("1 + 2 / 0", "Dividing by zero" ),
                                              ("1 ++ 2", "Spaces are missed" ),
                                              ("! + 2", "You entered invalid symbols" ),
                                              ("5 - w", "You entered alphabetic symbols"),
                                              (' - ( 3 + 4 ) * 2 + 5', 'Number is missing at the start of line'),
                                              ("25 - 3 * ( 3 + 5 ) -", "Number is missing at the end of line"),
                                              ("1 + 2 /  / 3", "Number is missing")])
def test_calc(example, expected):
    '''Negative tests-cases for calculator'''
    assert (calc(example)) == expected
