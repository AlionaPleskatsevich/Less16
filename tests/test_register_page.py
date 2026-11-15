from playwright.sync_api import expect
from pages.register_page import RegisterPage
from data.users import VALID_USERS
from data.users import INVALID_USERS


def test_open_register_page(page):
    register_page = RegisterPage(page)
    register_page.open_register_page()
    assert "login" in register_page.get_url()


def test_name_field_visible(page):
    register_page = RegisterPage(page)
    register_page.open_register_page()
    expect(register_page.name_input).to_be_visible()


def test_email_field_visible(page):
    register_page = RegisterPage(page)
    register_page.open_register_page()
    expect(register_page.email_input).to_be_visible()


def test_register_button_visible(page):
    register_page = RegisterPage(page)
    register_page.open_register_page()
    expect(register_page.signup_button).to_be_visible()


def test_valid_data(page):
    user = VALID_USERS[0]
    register_page = RegisterPage(page)
    register_page.open_register_page()
    register_page.enter_name(user["name"])
    register_page.enter_email(user["email"])
    register_page.click_signup()
    expect(page).to_have_url("https://automationexercise.com/signup")


def test_invalid_data(page):
    user = INVALID_USERS[0]
    register_page = RegisterPage(page)
    register_page.open_register_page()
    register_page.enter_name("")
    register_page.enter_email(user["email"])
    register_page.click_signup()
    expect(page).to_have_url("https://automationexercise.com/login")

