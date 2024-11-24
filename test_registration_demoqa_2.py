from selene import browser, be, have, by
import pytest
import os
import basic_date

image = os.path.abspath('./qfile.png')


@pytest.fixture
def personal_date(open_browser):
    browser.open('/')

    browser.element('#firstName').type('Yaroslav')
    browser.element('#lastName').type('Gusev')
    browser.element('#userEmail').type('SomeThing@email.com')
    browser.element(f'#gender-radio-{basic_date.SEX}').type(have.value(''))
    browser.element('#userNumber').type(f'{basic_date.TEL_NUMBER}')

    browser.element('#dateOfBirth').click().element(f'[value="{basic_date.MONTH}"]').click()
    browser.element('#dateOfBirth').element(f'[value="{basic_date.YEAR}"]').click()
    browser.element('.react-datepicker__month').element(by.text(f'{basic_date.DAY}')).click()

    browser.element('#subjectsInput').click().type('p').should(be.visible).press_enter()

    browser.element('#hobbiesWrapper').element(f'#hobbies-checkbox-1').type(have.value(''))
    browser.element('#hobbiesWrapper').element(f'#hobbies-checkbox-2').type(have.value(''))
    browser.element('#hobbiesWrapper').element(f'#hobbies-checkbox-3').type(have.value(''))

    browser.element('[id="uploadPicture"]').set_value(image)

    browser.element('#currentAddress').should(be.blank).type('text ' * 5)

    browser.element('#state').click()
    browser.element('#react-select-3-input').type(basic_date.STATE).should(be.visible).press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type(basic_date.CITY).should(be.visible).press_enter()
    browser.element('#submit').click()


def test_personal_data(personal_date):
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
