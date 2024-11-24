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
    browser.element('#genterWrapper').element(by.text(f'{basic_date.SEX}')).click()
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
    browser.element('.modal-body').should(have.text('Student Name')).should(have.text('Yaroslav Gusev'))
    browser.element('.modal-body').should(have.text('Student Email')).should(have.text('SomeThing@email.com'))
    browser.element('.modal-body').should(have.text('Gender')).should(have.text(f'{basic_date.SEX}'))
    browser.element('.modal-body').should(have.text('Mobile')).should(have.text(f'{basic_date.TEL_NUMBER}'))
    browser.element('.modal-body').should(have.text('Date of Birth')).should(have.text(
        f'{basic_date.DAY} {basic_date.MONTH_STR},{basic_date.YEAR}'))
    browser.element('.modal-body').should(have.text('Subjects')).should(have.text('Physics'))
    browser.element('.modal-body').should(have.text('Hobbies')).should(have.text('Sports, Reading, Music'))
    browser.element('.modal-body').should(have.text('Picture')).should(have.text('qfile.png'))
    browser.element('.modal-body').should(have.text('Address')).should(have.text('text text text text text'))
    browser.element('.modal-body').should(have.text('State and City')).should(have.text(
        f'{basic_date.STATE} {basic_date.CITY}'))
