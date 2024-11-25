from random import randint, choice
from secrets import choice

SEX = choice(['Male', 'Female', 'Other'])
TEL_NUMBER = randint(1000000000, 9999999999)
YEAR = randint(1950, 2010)
MONTH = choice(list({0: "January", 1: "February", 2: "March", 3: "April", 4: "May", 5: "June", 6: "July",
                     7: "August", 8: "September", 9: "October", 10: "November", 11: "December"}.items()))

STATE = choice(list({'NCR': ['Delhi', 'Gurgaon', 'Noida'],
                     'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
                     'Haryana': ['Karnal', 'Panipat'],
                     'Rajasthan': ['Jaipur', 'Jaiselmer']
                     }.items()))
CITY = choice(STATE[1])


def is_leap_year(year):
    return year % 4 == 0 and not year % 100 == 0 or year % 400 == 0


def days_in_month(month_index, year):
    if month_index in [0, 2, 4, 6, 7, 9, 11]:
        return 31
    elif month_index == 1:
        return 29 if is_leap_year(year) else 28
    else:
        return 30


BIRTHDAY_DAY = randint(1, days_in_month(MONTH[0], YEAR))
