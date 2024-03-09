from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Cart(Page):
    CART_EMPTY_MESSAGE = (By.XPATH, "//h1[contains(@class,'styles__StyledHeading')]")
    CANDLE_TEXT = (By.XPATH, "//div[text()='22oz Vanilla Cupcake Original Large Jar Candle - Yankee Candle']")

    def verify_cart_icon(self):
        self.wait_element_visible(*self.CART_EMPTY_MESSAGE)
        assert self.driver.find_element(*self.CART_EMPTY_MESSAGE).is_displayed()

    def verify_cart_and_check_out(self, expected_text):
        self.verify_text(expected_text, *self.CANDLE_TEXT)

