import pytest
from check_reg_term import check_example


@pytest.mark.parametrize("example,expected", [("facebook..com", "Wrong site name"),
                                              ("facebook.", "Unfinished name"),
                                              ("facebookcom", "Check site name")])
def test_check_example(example, expected):
    '''Negative  test-cases  for  whois  library'''
    assert (check_example(example)) == expected
