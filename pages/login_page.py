from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("login"), "Correct login page isn't displayed"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.fill_text_field(email, *LoginPageLocators.REGISTER_EMAIL_ADDRESS)
        self.fill_text_field(password, *LoginPageLocators.REGISTER_PASSWORD)
        self.fill_text_field(password, *LoginPageLocators.REGISTER_CONFIRM_PASSWORD)
        self.click_on_the_element(*LoginPageLocators.REGISTER_BUTTON)
