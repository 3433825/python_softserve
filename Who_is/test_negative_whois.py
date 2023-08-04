import pytest
from Registration.check_registration_term import check_site


@pytest.mark.parametrize("example,expected", [("facebook..com", "Two points in a row"),
                                              ("facebook.", "Unfinished name"),
                                              ("facebookcom", "Check site name")])
def test_check_example(example, expected):
    '''Negative  test-cases  for  whois  library'''

    assert check_site(example) == expected
