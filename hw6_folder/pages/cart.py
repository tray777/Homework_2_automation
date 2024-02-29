from selenium.webdriver.common.by import By
from pages.base_page import Page


class Cart(Page):
    CART_EMPTY_MESSAGE = (By.XPATH, "//h1[contains(@class,'styles__StyledHeading')]")

    def verify_cart_icon(self):
        assert self.driver.find_element(*self.CART_EMPTY_MESSAGE).is_displayed()
