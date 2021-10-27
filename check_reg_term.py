import whois
from datetime import datetime

def check_site(site, date_test):
    ERR_MESS_TWO_POINTS = "Two points in a row"
    ERR_MESS_UNFINISHED_NAME = "Unfinished name"
    ERR_MESS_CHECK_SITE_NAME = "Check site name"
   # ERR_MESS_NUM_DAYS = "The number of days must be greater than 0"

    if site.rfind("..") != -1:
        return ERR_MESS_TWO_POINTS
    elif site.endswith("."):
        return ERR_MESS_UNFINISHED_NAME
    elif site.rfind(".") == -1:
        return ERR_MESS_CHECK_SITE_NAME
    else:
        date_time_expire_obj = whois.whois(site).expiration_date
        if isinstance(date_time_expire_obj, list):
            date_time_expire = date_time_expire_obj[0].date()
        else:
            date_time_expire = date_time_expire_obj.date()

        date_requested = datetime.strptime(date_test, '%d-%m-%Y').date()
        days_end_reg_fr_test = (date_time_expire - date_requested).days
        return days_end_reg_fr_test
