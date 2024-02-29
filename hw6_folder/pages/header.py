from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_ICON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CLICK_CART_ICON = (By.XPATH, "//a[@data-test='@web/CartLink']")

    def search_product(self):
        self.input_text('coffee', *self.SEARCH_FIELD)
        self.click(*self.SEARCH_ICON)
        sleep(6)

    def click_on_cart_icon(self):
        self.click(*self.CLICK_CART_ICON)
        sleep(6)
        #self.wait.until(EC.element_to_be_clickable(CLICK_CART_ICON), message='cart icon not clicked')