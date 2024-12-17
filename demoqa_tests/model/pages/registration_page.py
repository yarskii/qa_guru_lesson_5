from selene import browser, be, have, by


class RegistrationPage:

    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.fullscreen_window()

    def fill_full_name(self, first_name, last_name):
        browser.element('#firstName').type(first_name)
        browser.element('#lastName').type(last_name)

    def fill_email(self, email):
        browser.element('#userEmail').type(email)

    def fill_gender(self, gender):
        browser.element('#genterWrapper').element(by.text(gender)).click()

    def fill_telephone_number(self, telephone_number):
        browser.element('#userNumber').type(telephone_number)

    def fill_date_of_birth(self, day, month, year):
        browser.element('#dateOfBirth').click().element(f'[value="{month - 1}"]').click()
        browser.element('#dateOfBirth').element(f'[value="{year}"]').click()
        browser.element('.react-datepicker__month').element(by.text(f'{day}')).click()

    def fill_subjects(self, subject):
        browser.element('#subjectsInput').click().type(subject).should(be.visible).press_enter()

    def fill_hobbies(self, sports, reading, music):
        browser.element('#hobbiesWrapper').element(by.text(sports)).click()
        browser.element('#hobbiesWrapper').element(by.text(reading)).click()
        browser.element('#hobbiesWrapper').element(by.text(music)).click()

    def fill_image(self, image):
        browser.element('[id="uploadPicture"]').set_value(image)

    def fill_current_address(self, current_address):
        browser.element('#currentAddress').should(be.blank).type(current_address)

    def fill_state_and_city(self, state, city):
        browser.element('#state').click()
        browser.element('#react-select-3-input').type(state).should(be.visible).press_enter()
        browser.element('#city').click()
        browser.element('#react-select-4-input').type(city).should(be.visible).press_enter()

    def submit_button(self):
        browser.element('#submit').click()

    def should_registered_user_with(self, full_name, email, gender, telephone,
                                    date_of_birth, subjects, hobby, image, address, state_and_city):
        browser.element('.modal-content').should(have.text('Thanks for submitting the form'))
        (browser.element('.modal-content').all('td').
         even.should(have.exact_texts(full_name, email, gender, f'{telephone}',
                                      date_of_birth, subjects, hobby, image, address, state_and_city
                                      )))
