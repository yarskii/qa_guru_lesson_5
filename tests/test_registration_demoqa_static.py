import os
from demoqa_tests.model.pages.registration_page import RegistrationPage


def test_personal_date_static(open_browser):
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_full_name('Yaroslav', 'Gusev')
    registration_page.fill_email('SomeThing@email.com')
    registration_page.fill_gender('Male')
    registration_page.fill_telephone_number('1111111111')
    registration_page.fill_date_of_birth(15, 3, 1931)
    registration_page.fill_subjects('Physics')
    registration_page.fill_hobbies('Sports', 'Reading', 'Music')
    registration_page.fill_image(os.path.abspath('../resources/image/qfile.png'))
    registration_page.fill_current_address('text ' * 5)
    registration_page.fill_state_and_city('NCR', 'Delhi')

    registration_page.submit_button()

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
