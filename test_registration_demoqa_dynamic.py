from selene import browser, be, have, by
import os
import basic_data

image = os.path.abspath('qfile.png')


def test_personal_date(open_browser):
    browser.open('/')

    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element('#firstName').type(f'{basic_data.FIRST_NAME}')
    browser.element('#lastName').type(f'{basic_data.LAST_NAME}')
    browser.element('#userEmail').type(f'{basic_data.EMAIL}')
    browser.element('#genterWrapper').element(by.text(f'{basic_data.SEX}')).click()
    browser.element('#userNumber').type(f'{basic_data.TEL_NUMBER}')

    browser.element('#dateOfBirth').click().element(f'[value="{basic_data.MONTH}"]').click()
    browser.element('#dateOfBirth').element(f'[value="{basic_data.YEAR}"]').click()
    browser.element('.react-datepicker__month').element(by.text(f'{basic_data.DAY}')).click()

    browser.element('#subjectsInput').click().type('p').should(be.visible).press_enter()

    browser.element('#hobbiesWrapper').element(f'#hobbies-checkbox-1').type(have.value(''))
    browser.element('#hobbiesWrapper').element(f'#hobbies-checkbox-2').type(have.value(''))
    browser.element('#hobbiesWrapper').element(f'#hobbies-checkbox-3').type(have.value(''))

    browser.element('[id="uploadPicture"]').set_value(image)

    browser.element('#currentAddress').should(be.blank).type(f'{basic_data.CURRENT_ADDRESS}')

    browser.element('#state').click()
    browser.element('#react-select-3-input').type(basic_data.STATE[0]).should(be.visible).press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type(basic_data.CITY).should(be.visible).press_enter()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text(f'{basic_data.STUDENT}'))
    browser.element('.modal-body').should(have.text(f'{basic_data.EMAIL}'))
    browser.element('.modal-body').should(have.text(f'{basic_data.SEX}'))
    browser.element('.modal-body').should(have.text(f'{basic_data.TEL_NUMBER}'))
    browser.element('.modal-body').should(
        have.text(f'{basic_data.DAY} {basic_data.MONTH_STR.get(basic_data.MONTH)},{basic_data.YEAR}'))
    browser.element('.modal-body').should(have.text('Physics'))
    browser.element('.modal-body').should(have.text('Sports, Reading, Music'))
    browser.element('.modal-body').should(have.text('qfile.png'))
    browser.element('.modal-body').should(have.text(f'{basic_data.CURRENT_ADDRESS}'))
    browser.element('.modal-body').should(have.text(f'{basic_data.STATE[0]} {basic_data.CITY}'))
