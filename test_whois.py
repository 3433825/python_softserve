import pytest
from days_left import days_to_expire

@pytest.mark.parametrize("example,expected", [("facebook.com", 30),
                                              ("rozetka.com.ua", 30),
                                              ("docs.python.org", 30),
                                              ("pythonru.com", 30),
                                              ("career.softserveinc.com", 30),
                                              ("compassd.com.ua", 30)])
def test_days_left(example, expected):
    assert (days_to_expire(example)) > expected
