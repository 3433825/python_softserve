import pytest
from check_reg_term import check_example

@pytest.mark.parametrize("example,expected", [("facebook.com", 3447),
                                              ("rozetka.com.ua", 3376),
                                              ("docs.python.org", 158),
                                              ("pythonru.com", 360),
                                              ("career.softserveinc.com", 1040),
                                              ("compassd.com.ua", 270)])
def test_check_example(example, expected):
    '''Positive test-cases for  whois library'''
    assert (check_example(example)) == expected
