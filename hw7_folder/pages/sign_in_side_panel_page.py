from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SignInSidePanelPage(Page):

    CLICK_ACCOUNT = (By.XPATH, "//span[text()='Sign in' and contains(@class,'styles__ListItemText')]")

    def click_on_account_sign_in(self):
        self.wait_element_clickable_click(*self.CLICK_ACCOUNT)
