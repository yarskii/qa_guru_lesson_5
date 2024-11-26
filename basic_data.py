from random import randint, choice
from faker import Faker

FIRST_NAME = Faker().first_name()
LAST_NAME = Faker().last_name()
STUDENT = f'{FIRST_NAME} {LAST_NAME}'
EMAIL = Faker().email()
SEX = choice(['Male', 'Female', 'Other'])
TEL_NUMBER = randint(1000000000, 9999999999)

DATE = Faker().date().split('-')
YEAR = DATE[0]
MONTH = int(DATE[1]) - 1
DAY = int(DATE[2])
MONTH_STR = {0: "January", 1: "February", 2: "March", 3: "April", 4: "May", 5: "June", 6: "July",
             7: "August", 8: "September", 9: "October", 10: "November", 11: "December"}

CURRENT_ADDRESS = Faker().address().replace('\n', " ")

STATE = choice(list({'NCR': ['Delhi', 'Gurgaon', 'Noida'],
                     'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
                     'Haryana': ['Karnal', 'Panipat'],
                     'Rajasthan': ['Jaipur', 'Jaiselmer']
                     }.items()))
CITY = choice(STATE[1])
