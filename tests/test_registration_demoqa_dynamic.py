import allure

from demoqa_tests.model.pages.registration_page import RegistrationPage
from resources import basic_data
from resources.basic_data import IMAGE


@allure.tag('web')
@allure.feature("Регистрируем нового пользователя")
@allure.story("Успешная регистрация")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Yaroslav Gusev")
@allure.description("Тест для проверки ввода данных и проверки")
@allure.link("https://demoqa.com/", name="Testing")
def test_personal_date_dynamic(open_demoqa):
    registration_page = RegistrationPage()

    with allure.step("Открываем главную страницу регистрации"):
        registration_page.open()

    with allure.step("Вводим имя и фамилию"):
        registration_page.fill_full_name(basic_data.FIRST_NAME, basic_data.LAST_NAME)

    with allure.step("Вводим адрес электронной почты"):
        registration_page.fill_email(basic_data.EMAIL)

    with allure.step("Выбираем пол"):
        registration_page.fill_gender(basic_data.SEX)

    with allure.step("Вводим номер телефона"):
        registration_page.fill_telephone_number(basic_data.TEL_NUMBER)

    with allure.step("Выбираем дату рождения"):
        registration_page.fill_date_of_birth(basic_data.DAY, basic_data.MONTH, basic_data.YEAR)

    with allure.step("Выбираем изучаемы предмет(ы)"):
        registration_page.fill_subjects('Physics')

    with allure.step("Выбираем увлечения"):
        registration_page.fill_hobbies('Sports', 'Reading', 'Music')

    with allure.step("Загружаем фотографию"):
        registration_page.fill_image(IMAGE)

    with allure.step("Вводим адрес проживания"):
        registration_page.fill_current_address(basic_data.CURRENT_ADDRESS)

    with allure.step("Выбираем штат и город"):
        registration_page.fill_state_and_city(basic_data.STATE[0], basic_data.CITY)

    with allure.step("Отправляем данные"):
        registration_page.submit_button()

    with allure.step("Проверка введенных данных"):
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
