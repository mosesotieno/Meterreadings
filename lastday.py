from datetime import date
from datetime import datetime


def last_day_of_month(year, month):
    """ Work out the last day of the month """
    last_days = [31, 30, 29, 28, 27]
    for i in last_days:
        try:
            end = datetime(year, month, i)
        except ValueError:
            continue
        else:
            return end.date()
    return None


todays_date = date.today()
cyear = todays_date.year
cmonth = todays_date.month
lastday = last_day_of_month(cyear, cmonth)
