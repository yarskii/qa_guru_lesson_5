from random import randint, choice
from secrets import choice
from days_in_month import days_in_month

SEX = choice(['Male', 'Female', 'Other'])
TEL_NUMBER = randint(1000000000, 9999999999)
YEAR = randint(1950, 2010)
MONTH = choice(list({0: "January", 1: "February", 2: "March", 3: "April", 4: "May", 5: "June", 6: "July",
                     7: "August", 8: "September", 9: "October", 10: "November", 11: "December"}.items()))
BIRTHDAY_DAY = randint(1, days_in_month(MONTH[0], YEAR))

STATE = choice(list({'NCR': ['Delhi', 'Gurgaon', 'Noida'],
                     'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
                     'Haryana': ['Karnal', 'Panipat'],
                     'Rajasthan': ['Jaipur', 'Jaiselmer']
                     }.items()))
CITY = choice(STATE[1])
