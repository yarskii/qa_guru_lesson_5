from random import randint

SEX = randint(1, 3)
TEL_NUMBER = randint(1000000000, 9999999999)
YEAR = randint(1900, 2100)
MONTH = randint(0, 11)


def date_of_born():
    if YEAR % 4 == 0 and not YEAR % 100 == 0 or YEAR % 400 == 0:
        if MONTH in [0, 2, 4, 6, 7, 9, 11]:
            return randint(1, 31)
        elif MONTH == 1:
            return randint(1, 29)
        else:
            return randint(1, 30)
    else:
        if MONTH in [0, 2, 4, 6, 7, 9, 11]:
            return randint(1, 31)
        elif MONTH == 1:
            return randint(1, 28)
        else:
            return randint(1, 30)


DAY = date_of_born()

all_state = ['NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan']
NCR = ['Delhi', 'Gurgaon', 'Noida']
Uttar_Pradesh = ['Agra', 'lucknow', 'Merrut']
Haryana = ['Karnal', 'Panipat']
Rajasthan = ['Jaipur', 'Jaiselmer']

STATE = all_state[randint(0, 3)]


def my_city():
    if STATE == 'NCR':
        return NCR[randint(0, 2)]
    elif STATE == 'Uttar Pradesh':
        return Uttar_Pradesh[randint(0, 2)]
    elif STATE == 'Haryana':
        return Haryana[randint(0, 1)]
    elif STATE == 'Rajasthan':
        return Rajasthan[randint(0, 1)]


CITY = my_city()
