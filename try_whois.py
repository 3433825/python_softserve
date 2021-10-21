def expect_whois(example_site):
    import datetime
    import whois

    date_time_expire_obj = whois.whois(example_site).expiration_date
    if isinstance(date_time_expire_obj, list):
        date_time_expire  = date_time_expire_obj[0].date()
    else:
        date_time_expire = date_time_expire_obj.date()

    actual_date = datetime.datetime.today().date()
    days_left = date_time_expire - actual_date

    return days_left.days



