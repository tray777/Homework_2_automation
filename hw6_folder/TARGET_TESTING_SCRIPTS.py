from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target_main_page(context):
    context.app.main_page.open_main()


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.app.header.click_on_cart_icon()


@then("Verify {cart_empty_message} text displays")
def verify_cart_icon(context, cart_empty_message):
    context.app.cart.verify_cart_icon()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product()


@then('Search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    context.app.search_results_page.verify_search_results_correct(expected_result)


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context, expected_part_url):
    context.app.search_results_page.verify_search_results_page_url(expected_part_url)