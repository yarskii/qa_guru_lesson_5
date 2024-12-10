import dataclasses

from resources import basic_data


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    telephone_number: str
    date_of_birth: list[int]
    subject: str
    hobbies: list[str]
    image: any
    current_address: str
    state_and_city: list[str]


admin = User(first_name=f'{basic_data.FIRST_NAME}',
             last_name=f'{basic_data.LAST_NAME}',
             gender=f'{basic_data.SEX}',
             email=f'{basic_data.EMAIL}',
             telephone_number=f'{basic_data.TEL_NUMBER}',
             date_of_birth=[basic_data.DAY, basic_data.MONTH, basic_data.YEAR],
             subject='Physics',
             hobbies=['Sports', 'Reading', 'Music'],
             image=basic_data.IMAGE,
             current_address=f'{basic_data.CURRENT_ADDRESS}',
             state_and_city=[basic_data.STATE[0], basic_data.CITY],
             )
