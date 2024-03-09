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


@when('Click on sign in icon')
def click_on_sign_in(context):
    context.app.header.click_on_sign_in()


@when('Click on Account sign in icon')
def click_on_account_sign_in(context):
    context.app.sign_in_side_panel_page.click_on_account_sign_in()


@then('Verify {expected_sign_in_form} message displays accurately')
def verify_by_sign_in(context, expected_sign_in_form):
    context.app.sign_in_page.verify_by_sign_in(expected_sign_in_form)


@when("Type search word {product} into textbox")
def click_on_search_words(context, product):
    context.app.header.click_on_search_words(product)


@when("Click the search icon")
def click_the_search_icon(context):
    context.app.header.click_the_search_icon()


@when("Click Add to cart button")
def click_on_cart_button(context):
    context.app.add_to_cart_page.click_on_cart_button()


@when("Click on Pick Up button")
def click_on_pick_up_button(context):
    context.app.add_to_cart_side_panel_page.click_on_pick_up_button()


@when("Click Side Panel Add to Cart button")
def click_side_panel_add(context):
    context.app.add_to_cart_side_panel_page.click_side_panel_add()


@when("click on View cart & check out")
def click_on_view_cart_and_check_out(context):
    context.app.add_to_cart_side_panel_page.click_on_view_cart_and_check_out()


@then("Verify {expected_text} message is shown")
def verify_cart_and_check_out(context, expected_text):
    context.app.cart.verify_cart_and_check_out(expected_text)

