from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BENEFIT_BOXES = (By.XPATH, "//img[contains(@class,'styles__BenefitCardImage')]")
LINK_BOXES = (By.XPATH, "//div[@class='grid_6']")
LINK_INFO_BOXES = (By.CSS_SELECTOR, "[class*=grid_4]")
BROWSE_TEXT = (By.XPATH, "//h2[text()='Browse all Help pages']")

@given('Open Target main page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')


@when("Type search word {product} into textbox")
def click_on_search_words(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    sleep(6)


@when("Click the search icon")
def click_the_search_icon(context):
    context.driver.find_element(By.XPATH, "//button[contains(@class,'styles__SearchButton')]").click()
    sleep(6)


@when("Click Add to cart button")
def click_on_cart_button(context):
    context.driver.find_element(By.XPATH, "//button[@id='addToCartButtonOrTextIdFor89130241']").click()
    sleep(6)


@when("Click on Pick Up button")
def click_on_pick_up_button(context):
    context.driver.find_element(By.XPATH, "//button[contains(@aria-label,'pickup')]").click()
    sleep(6)


@when("Click Side Panel Add to Cart button")
def click_side_panel_add(context):
    context.driver.find_element(By.XPATH, "//button[@type='button' and contains(@aria-label,'Add to cart for 22oz')]").click()
    sleep(6)


@when("click on View cart & check out")
def click_on_view_cart_and_check_out(context):
    context.driver.find_element(By.XPATH, "//a[text()='View cart & check out']").click()
    sleep(6)


@then("Verify {expected_text} message is shown")
def verify_cart_and_check_out(context, expected_text):
    assert context.driver.find_element(By.XPATH, "//div[text()='22oz Vanilla Cupcake Original Large Jar Candle - Yankee Candle']").is_displayed()
    sleep(6)


@given('Open Target circle page')
def open_target_main_page(context):
    context.driver.get('https://www.target.com/circle')

@then('Verify {box_amount} benefit boxes are shown')
def verify_5_benefit_boxes(context, box_amount):
    box_amount = int(box_amount)
    benefit_boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(benefit_boxes) == box_amount, f'Expected {box_amount} links, but got {len(benefit_boxes)}'


@given('Open Target help UI page')
def open_target_help_ui(context):
    context.driver.get('https://help.target.com/help')


@then('Verify {target_help} text is shown')
def verify_cart_and_check_out(context, target_help):
    assert context.driver.find_element(By.XPATH, "//h2[@class='custom-h2']").is_displayed()
    sleep(6)


@then('Verify {link_help_boxes} link boxes are shown')
def verify_6_buttons(context, link_help_boxes):
    link_help_boxes = int(link_help_boxes)
    link_boxes = context.driver.find_elements(*LINK_BOXES)
    assert len(link_boxes) == link_help_boxes, f'Expected {link_help_boxes} links, but got {len(link_boxes)}'


@then('Verify {info_box} information boxes are shown')
def verify_info_buttons(context, info_box):
    info_box = int(info_box)
    link_info_boxes = context.driver.find_elements(*LINK_INFO_BOXES)
    assert len(link_info_boxes) == info_box, f'Expected {info_box} links, but got {len(link_info_boxes)}'


@then('Verify {help_page_text} text is visible')
def verify_info_buttons(context, help_page_text):
    #assert context.driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']").is_displayed()
    assert context.driver.find_element(*BROWSE_TEXT).is_displayed()
    sleep(6)
