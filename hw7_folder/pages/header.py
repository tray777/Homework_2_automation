from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CLICK_CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")
    CLICK_SIGN_IN = (By.XPATH, "//span[contains(@class,'styles__LinkText')]")
    CLICK_SEARCH_ICON = (By.XPATH, "//button[contains(@class,'styles__SearchButton')]")

    def search_product(self):
        self.input_text('coffee', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)

    def click_on_cart_icon(self):
        self.wait_element_clickable(*self.CLICK_CART_ICON)

    def click_on_sign_in(self):
        self.wait_element_clickable_click(*self.CLICK_SIGN_IN)

    def click_on_search_words(self, product):
        self.input_text(product, *self.SEARCH_FIELD)

    def click_the_search_icon(self):
        self.wait_element_clickable_click(*self.CLICK_SEARCH_ICON)

