import pytest
from check_reg_term import check_example

@pytest.mark.parametrize("site, date_test, expected", [("facebook.com", "01-01-2022", 3375),
                                              (("facebook.com", "01-01-2023", 3010)),
                                              (("facebook.com", "01-01-2024", 2645))])
def test_check_example(site, date_test, expected):
    '''Positive test-cases for  whois library'''

    assert (check_example(site, date_test)) == expected

