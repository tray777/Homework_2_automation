from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']").click()


@then('Verify “Your cart is empty” message is shown')
def verify_cart_icon(context):
    expected_cart_message = 'Your cart is empty'
    actual_cart_message = context.driver.find_element(By.XPATH, "//h1[contains(@class,'styles__StyledHeading')]").text
    assert expected_cart_message == actual_cart_message, f'Expected message {expected_cart_message} not in {actual_cart_message}'
    print("TestCase Cart is Empty: Pass")


@when('Click on sign in icon')
def click_on_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[contains(@class,'styles__LinkText')]").click()


@when('Click on Account sign in icon')
def click_on_account_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[text()='Sign in' and contains(@class,'styles__ListItemText')]").click()


@then('Verify “By signing in, you agree to the following:” message is shown')
def verify_by_sign_in(context):
    expected_sign_in_form = 'By signing in, you agree to the following:'
    actual_sign_in_form = context.driver.find_element(By.XPATH, "//p[text()='By signing in, you agree to the following:']").text
    assert expected_sign_in_form == actual_sign_in_form, f'Expected message {expected_sign_in_form} not in {actual_sign_in_form}'
    print("TestCase User Sign In: Pass")


@when("Type search word 'yankee candles' into textbox")
def click_on_search_words(context):
    search_word = 'yankee candles'
    context.driver.find_element(By.ID, 'search').send_keys(search_word)


@when("Click the search icon")
def click_the_search_icon(context):
    context.driver.find_element(By.XPATH, "//button[contains(@class,'styles__SearchButton')]").click()


@when("Click Add to cart button")
def click_on_cart_button(context):
    context.driver.find_element(By.XPATH, "//button[@id='addToCartButtonOrTextIdFor89130241']").click()


@when("Click on Pick Up button")
def click_on_pick_up_button(context):
    context.driver.find_element(By.XPATH, "//button[contains(@aria-label,'pickup')]").click()


@when("Click Side Panel Add to Cart button")
def click_side_panel_add(context):
    context.driver.find_element(By.XPATH, "//button[@type='button' and contains(@aria-label,'Add to cart for 22oz')]").click()


@when("click on View cart & check out")
def click_on_view_cart_and_check_out(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()


@then("Verify “22oz Vanilla Cupcake Original Large Jar Candle - Yankee Candle” message is shown")
def verify_cart_and_check_out(context):
    expected_text = '22oz Vanilla Cupcake Original Large Jar Candle - Yankee Candle'
    actual_text = context.driver.find_element(By.XPATH, "//div[text()='22oz Vanilla Cupcake Original Large Jar Candle - Yankee Candle']").text
    assert expected_text in actual_text, f"Expected word {expected_text} not in {actual_text}"
    print('Verify item in Cart: pass')
