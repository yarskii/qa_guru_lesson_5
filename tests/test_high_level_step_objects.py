import allure

from demoqa_tests.data import users
from demoqa_tests.model.pages.simple_user_registration_page import SimpleUserRegistrationPage
from resources import basic_data


def test_personal_date_static_high(open_demoqa):
    registration_page = SimpleUserRegistrationPage()

    with allure.step('Открываем страницу регистрации пользователя DemoQA'):
        registration_page.open()

    with allure.step('Вводим данные пользователя'):
        registration_page.register(users.admin)

    with allure.step('Проверяем введенные данные'):
        (registration_page.
        should_registered_user_with(
            basic_data.STUDENT,
            basic_data.EMAIL,
            basic_data.SEX,
            basic_data.TEL_NUMBER,
            f'{str(basic_data.DAY).zfill(2)} {basic_data.MONTH_STR.get(basic_data.MONTH)},{basic_data.YEAR}',
            'Physics',
            'Sports, Reading, Music',
            'qfile.png',
            basic_data.CURRENT_ADDRESS,
            f'{basic_data.STATE[0]} {basic_data.CITY}'
        ))
