from datetime import datetime

def check_end_date(date_end):

    date_end_registration = datetime.strptime(date_end, '%Y-%m-%d').date()
    actual_date_with_date_end = datetime.today().date()
    days_before_date_end_registration = (date_end_registration - actual_date_with_date_end).days
    print(actual_date_with_date_end)

    return days_before_date_end_registration
