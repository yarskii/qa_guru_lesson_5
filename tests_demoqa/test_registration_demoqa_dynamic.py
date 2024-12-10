from demoqa_tests.registration_page import RegistrationPage
from resources import basic_data
from resources.basic_data import IMAGE


def test_personal_date_dynamic(open_browser):
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_full_name(basic_data.FIRST_NAME, basic_data.LAST_NAME)
    registration_page.fill_email(basic_data.EMAIL)
    registration_page.fill_gender(basic_data.SEX)
    registration_page.fill_telephone_number(basic_data.TEL_NUMBER)
    registration_page.fill_date_of_birth(basic_data.DAY, basic_data.MONTH, basic_data.YEAR)
    registration_page.fill_subjects('Physics')
    registration_page.fill_hobbies('Sports', 'Reading', 'Music')
    registration_page.fill_image(IMAGE)
    registration_page.fill_current_address(basic_data.CURRENT_ADDRESS)
    registration_page.fill_state_and_city(basic_data.STATE[0], basic_data.CITY)

    registration_page.submit_button()

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
