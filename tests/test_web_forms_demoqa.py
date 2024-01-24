import pytest
from selene import browser, be, have

def test_form():
    browser.open('/')
    browser.element('#firstName').type('ИМЯ')
    browser.element('#lastName').type('ФАМИЛИЯ')
    browser.element('#userEmail').type('EMAIL')
    browser.element('#gender-radio-1').click()