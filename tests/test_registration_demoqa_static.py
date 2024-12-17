import allure
from demoqa_tests.model.pages.registration_page import RegistrationPage
from resources.basic_data import IMAGE


def test_personal_date_static(open_demoqa):
    registration_page = RegistrationPage()

    with allure.step("Открываем главную страницу регистрации"):
        registration_page.open()

    with allure.step("Вводим Yaroslav и Gusev"):
        registration_page.fill_full_name('Yaroslav', 'Gusev')

    with allure.step("Вводим SomeThing@email.com"):
        registration_page.fill_email('SomeThing@email.com')

    with allure.step("Выбираем Male"):
        registration_page.fill_gender('Male')

    with allure.step("Вводим 1111111111"):
        registration_page.fill_telephone_number('1111111111')

    with allure.step("Вводим 15, 3, 1931"):
        registration_page.fill_date_of_birth(15, 3, 1931)

    with allure.step("Выбираем Physics"):
        registration_page.fill_subjects('Physics')

    with allure.step("Выбираем 'Sports', 'Reading', 'Music'"):
        registration_page.fill_hobbies('Sports', 'Reading', 'Music')

    with allure.step("Загружаем фотографию"):
        registration_page.fill_image(IMAGE)

    with allure.step("Вводим 'text' * 5"):
        registration_page.fill_current_address('text ' * 5)

    with allure.step("Выбираем NCR и Delhi"):
        registration_page.fill_state_and_city('NCR', 'Delhi')

    with allure.step("Отправляем данные"):
        registration_page.submit_button()

    with allure.step("Проверка пользовательских данных"):
        registration_page.should_registered_user_with('Yaroslav Gusev',
                                                      'SomeThing@email.com',
                                                      'Male',
                                                      '1111111111',
                                                      '15 March,1931',
                                                      'Physics',
                                                      'Sports, Reading, Music',
                                                      'qfile.png',
                                                      'text text text text text',
                                                      'NCR Delhi')
