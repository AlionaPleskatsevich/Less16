from pages.base_page import BasePage


class RegisterPage(BasePage):
    URL = "https://automationexercise.com/login"

    def __init__(self, page):
        super().__init__(page)
        self.register_invait = page.get_by_role("heading", name="New User Signup!")
        self.name_input = page.get_by_role("textbox", name="Name")
        self.email_input = page.locator('input[data-qa="signup-email"]')
        self.signup_button = page.get_by_role("button", name="Signup")


    def open_register_page(self):
        self.open(self.URL)

    def enter_name(self, name):
        self.name_input.fill(name)

    def enter_email(self, email):
        self.email_input.fill(email)

    def click_signup(self):
        self.signup_button.click()

    def signup(self, name, email):
        self.enter_name(name)
        self.enter_email(email)
        self.click_signup()
