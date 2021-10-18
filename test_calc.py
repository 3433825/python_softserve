import pytest
from calculator import calc
'''Test cases for calculator'''
'''   positive and negative '''

@pytest.mark.parametrize("example,expected", [("1 + 2", 3),
                                              ("5 - 3", 2),
                                              ("2 * 3", 6),
                                              ("10 / 4", 2.5),
                                              ("1 + 2 * 3", 7),
                                              ("2 * 3 + 4", 10),
                                              ("7 - 2 * 3", 1),
                                              ("7 * 2 - 3", 11),
                                              ("2 + 6 / 3", 4),
                                              ("6 / 3 + 2", 4),
                                              ("10 - 6 / 3", 8),
                                              ("10 / 2 - 3", 2),
                                              ("2 * 3 / 4", 1.5),
                                              ("2 * 3 / 4 * 3", 4.5),
                                              ("3 * 4 / 2 * 2", 12),
                                              ("3 * 4 / ( 2 * 2 )", 3),
                                              ("8 / 2 * 2", 8),
                                              ("1 + 2 * ( 3 + 4 )", 15),
                                              ("2 * ( 3 + 4 ) + 4", 18),
                                              ("( 3 + 4 ) * 2 + 5", 19),
                                              ("25 - 3 * ( 3 + 5 )", 1),
                                              ("( 3 + 5 ) * 3 - 15", 9),
                                              ("3 * ( 3 + 5 ) - 10", 14),
                                              ("2 + 16 / ( 3 + 5 )", 4),
                                              ("( 3 + 5 ) / 4 + 2", 4),
                                              ("! + 2", "You entered invalid symbols" ),
                                              ("5 - w", "You entered alphabetic symbols"),
                                              (' - ( 3 + 4 ) * 2 + 5 = 29', 'Number is missing at the start of line'),
                                              ("25 - 3 * ( 3 + 5 )-", "Number is missing at the end of line"),
                                              ("1 + 2 // 3", "Number is missing")])
def test_calc(example, expected):
    assert (calc(example)) == expected
