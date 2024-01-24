from selene import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_open():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    
    yield

    browser.close()
