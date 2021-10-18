def days_to_expire(example_site):
    import datetime
    import whois

    date_time_expire_obj = whois.whois(example_site).expiration_date
    if type(date_time_expire_obj) is list:
        date_time_expire  = date_time_expire_obj[0].date()
    else:
        date_time_expire = date_time_expire_obj.date()

    actual_date = datetime.datetime.today().date()
    days_left = date_time_expire - actual_date

    return days_left.days