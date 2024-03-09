from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class AddToCartPage(Page):
    ADD_TO_CART = (By.XPATH, "//button[@id='addToCartButtonOrTextIdFor89130241']")

    def click_on_cart_button(self):
        
        self.wait_element_visible(*self.ADD_TO_CART)
        sleep(6)
        self.click(*self.ADD_TO_CART)

        #add_to_cart_button = context.wait.until(EC.element_to_be_clickable(ADD_TO_CART),message='add to cart not clicked')
        #context.driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
        #context.driver.find_element(*ADD_TO_CART).click()
