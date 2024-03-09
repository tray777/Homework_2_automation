from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SignInPage(Page):
    SIGN_IN_AGREE_MSG = (By.XPATH, "//p[text()='By signing in, you agree to the following:']")

    def verify_by_sign_in(self, expected_sign_in_form):
        self.wait_element_visible(*self.SIGN_IN_AGREE_MSG)