import pytest
from pages.login_page import LoginPage
import time


def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


@pytest.mark.need_review_custom_scenarios
def test_register_new_user(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.register_new_user(email=str(time.time())+"@fakemail.org", password='Qw11111111!')
    page.should_be_authorized_user()


@pytest.mark.need_review_custom_scenarios
def test_registered_user_authorization(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.auth_user(email='test12345@gmail.com', password='Qw1234567')
    page.should_be_authorized_user()