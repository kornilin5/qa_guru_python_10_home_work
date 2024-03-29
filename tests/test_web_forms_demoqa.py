import pytest
import os
from selene import browser, be, have


def test_form():
    browser.open('/')
    browser.element('#firstName').type('ИМЯ')
    browser.element('#lastName').type('ФАМИЛИЯ')
    browser.element('#userEmail').type('EMAIL@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element("#userNumber").type("2381491357")
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select [value="2"]').should(
        be.clickable).click()
    browser.element('.react-datepicker__year-select [value="1999"]').should(
        be.clickable).click()
    browser.element(
        '.react-datepicker__day.react-datepicker__day--017').should(
            be.clickable).click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture.form-control-file').send_keys(
        os.path.abspath('ZnugKfP5UJk.png'))
    browser.element("#currentAddress").type("ТУТ АДРЕСС")
    browser.element('#state').click()
    browser.element('#react-select-3-option-2').should(be.clickable).click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-1').should(be.clickable).click()
    browser.element('#submit').should(be.clickable).press_enter()
    browser.element('.table').all('td:nth-child(2)').should(
        have.texts('ИМЯ ФАМИЛИЯ',
                   'EMAIL@mail.ru', 
                   'Male', 
                   '2381491357',
                   '17 March,1999', 
                   'English', 
                   'Reading', 
                   'ZnugKfP5UJk.jpg',
                   'ТУТ АДРЕСС', 
                   'Haryana Panipat'))
