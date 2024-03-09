from pages.add_to_cart_page import AddToCartPage
from pages.add_to_cart_side_panel_page import AddToCartSidePanelPage
from pages.base_page import Page
from pages.cart import Cart
from pages.circle_page import CirclePage
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.sign_in_page import SignInPage
from pages.sign_in_side_panel_page import SignInSidePanelPage


class Application:

    def __init__(self, driver):
        self.add_to_cart_page = AddToCartPage(driver)
        self.add_to_cart_side_panel_page = AddToCartSidePanelPage(driver)
        self.page = Page(driver)
        self.cart = Cart(driver)
        self.circle_page = CirclePage(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.sign_in_page = SignInPage(driver)
        self.sign_in_side_panel_page = SignInSidePanelPage(driver)
