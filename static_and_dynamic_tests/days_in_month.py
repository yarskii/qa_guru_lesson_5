def is_leap_year(year):
    return year % 4 == 0 and not year % 100 == 0 or year % 400 == 0


def days_in_month(month_index, year):
    if month_index in [0, 2, 4, 6, 7, 9, 11]:
        return 31
    elif month_index == 1:
        return 29 if is_leap_year(year) else 28
    else:
        return 30
