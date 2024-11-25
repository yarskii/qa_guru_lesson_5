from selene import browser, be, have, by
import os
import basic_data

image = os.path.abspath('../qa_guru_lesson_5/images/qfile.png')


def test_personal_date_static(open_browser):
    browser.open('/')

    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element('#firstName').type('Yaroslav')
    browser.element('#lastName').type('Gusev')
    browser.element('#userEmail').type('SomeThing@email.com')
    browser.element('#genterWrapper').element(by.text('Male')).click()
    browser.element('#userNumber').type(f'1111111111')

    browser.element('#dateOfBirth').click().element('[value="2"]').click()
    browser.element('#dateOfBirth').element('[value="1931"]').click()
    browser.element('.react-datepicker__month').element(by.text('15')).click()

    browser.element('#subjectsInput').click().type('p').should(be.visible).press_enter()

    browser.element('#hobbiesWrapper').element(f'#hobbies-checkbox-1').type(have.value(''))
    browser.element('#hobbiesWrapper').element(f'#hobbies-checkbox-2').type(have.value(''))
    browser.element('#hobbiesWrapper').element(f'#hobbies-checkbox-3').type(have.value(''))

    browser.element('[id="uploadPicture"]').set_value(image)

    browser.element('#currentAddress').should(be.blank).type('text ' * 5)

    browser.element('#state').click()
    browser.element('#react-select-3-input').type('NCR').should(be.visible).press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type('Delhi').should(be.visible).press_enter()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text('Student Name')).should(have.text('Yaroslav Gusev'))
    browser.element('.modal-body').should(have.text('Student Email')).should(have.text('SomeThing@email.com'))
    browser.element('.modal-body').should(have.text('Gender')).should(have.text('Male'))
    browser.element('.modal-body').should(have.text('Mobile')).should(have.text('1111111111'))
    browser.element('.modal-body').should(have.text('Date of Birth')).should(have.text('15 March,1931'))
    browser.element('.modal-body').should(have.text('Subjects')).should(have.text('Physics'))
    browser.element('.modal-body').should(have.text('Hobbies')).should(have.text('Sports, Reading, Music'))
    browser.element('.modal-body').should(have.text('Picture')).should(have.text('qfile.png'))
    browser.element('.modal-body').should(have.text('Address')).should(have.text('text text text text text'))
    browser.element('.modal-body').should(have.text('State and City')).should(have.text('NCR Delhi'))


def test_personal_date_dynamic(open_browser):
    browser.open('/')

    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")

    browser.element('#firstName').type('Yaroslav')
    browser.element('#lastName').type('Gusev')
    browser.element('#userEmail').type('SomeThing@email.com')
    browser.element('#genterWrapper').element(by.text(f'{basic_data.SEX}')).click()
    browser.element('#userNumber').type(f'{basic_data.TEL_NUMBER}')

    browser.element('#dateOfBirth').click().element(f'[value="{basic_data.MONTH[0]}"]').click()
    browser.element('#dateOfBirth').element(f'[value="{basic_data.YEAR}"]').click()
    browser.element('.react-datepicker__month').element(by.text(f'{basic_data.BIRTHDAY_DAY}')).click()

    browser.element('#subjectsInput').click().type('p').should(be.visible).press_enter()

    browser.element('#hobbiesWrapper').element(f'#hobbies-checkbox-1').type(have.value(''))
    browser.element('#hobbiesWrapper').element(f'#hobbies-checkbox-2').type(have.value(''))
    browser.element('#hobbiesWrapper').element(f'#hobbies-checkbox-3').type(have.value(''))

    browser.element('[id="uploadPicture"]').set_value(image)

    browser.element('#currentAddress').should(be.blank).type('text ' * 5)

    browser.element('#state').click()
    browser.element('#react-select-3-input').type(basic_data.STATE[0]).should(be.visible).press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').type(basic_data.CITY).should(be.visible).press_enter()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text('Yaroslav Gusev'))
    browser.element('.modal-body').should(have.text('SomeThing@email.com'))
    browser.element('.modal-body').should(have.text(f'{basic_data.SEX}'))
    browser.element('.modal-body').should(have.text(f'{basic_data.TEL_NUMBER}'))
    browser.element('.modal-body').should(
        have.text(f'{basic_data.BIRTHDAY_DAY} {basic_data.MONTH[1]},{basic_data.YEAR}'))
    browser.element('.modal-body').should(have.text('Physics'))
    browser.element('.modal-body').should(have.text('Sports, Reading, Music'))
    browser.element('.modal-body').should(have.text('qfile.png'))
    browser.element('.modal-body').should(have.text('text text text text text'))
    browser.element('.modal-body').should(have.text(f'{basic_data.STATE[0]} {basic_data.CITY}'))
