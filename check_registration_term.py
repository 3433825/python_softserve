import whois
import datetime

def check_site(site):
    ERR_MESS_TWO_POINTS = "Two points in a row"
    ERR_MESS_UNFINISHED_NAME = "Unfinished name"
    ERR_MESS_CHECK_SITE_NAME = "Check site name"

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

        actual_date = datetime.datetime.today().date()
        days_end_reg_from_actual_date = (date_time_expire - actual_date).days
        return days_end_reg_from_actual_date

