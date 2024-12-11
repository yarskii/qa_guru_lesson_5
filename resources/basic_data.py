import os
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
MONTH = int(DATE[1])
DAY = int(DATE[2])
MONTH_STR = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July",
             8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

IMAGE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'resources/image/qfile.png'))

CURRENT_ADDRESS = Faker().address().replace('\n', " ")

STATE = choice(list({'NCR': ['Delhi', 'Gurgaon', 'Noida'],
                     'Uttar Pradesh': ['Agra', 'Lucknow', 'Merrut'],
                     'Haryana': ['Karnal', 'Panipat'],
                     'Rajasthan': ['Jaipur', 'Jaiselmer']
                     }.items()))
CITY = choice(STATE[1])
