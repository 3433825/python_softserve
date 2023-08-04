import pytest
from Registration.check_registration_term import check_site
from Registration.check_end_date_registration import check_end_date

@pytest.mark.parametrize("site, expected", [("rozetka.com.ua", "2031-01-18"),
                                              ("compassd.com.ua", "2022-07-18")])
def test_check_site(site, expected):
    '''Positive test-cases for  whois library'''

    assert check_site(site) == check_end_date(expected)

