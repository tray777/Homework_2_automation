from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class AddToCartSidePanelPage(Page):
    PICK_UP_BUTTON = (By.XPATH, "//button[contains(@aria-label,'pickup')]")
    SIDE_PANEL_ADD_CART_BUTTON = (By.XPATH, "//button[@type='button' and contains(@aria-label,'Add to cart for 22oz')]")
    VIEW_CART_CHECKOUT = (By.XPATH, "//a[text()='View cart & check out']")

    def click_on_pick_up_button(self):
        self.wait_element_clickable_click(*self.PICK_UP_BUTTON)

    def click_side_panel_add(self):
        self.wait_element_clickable_click(*self.SIDE_PANEL_ADD_CART_BUTTON)

    def click_on_view_cart_and_check_out(self):
        self.wait_element_clickable_click(*self.VIEW_CART_CHECKOUT)


