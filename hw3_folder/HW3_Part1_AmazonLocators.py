from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fproduct%2FB00009XVCZ%2Fref%3Dcm_cd_asin_lnk%2F%3Fie%3DUTF8%26redirect%3Dtrue%26ref_%3Dnav_ya_signin&prevRID=AVC3XHA6761T64T960B4&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')


#Amazon Logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon-logo')


#Create account text
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')


#'Your Name' textbox
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')


#'Mobile number or email' textbox
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')


#'Password' textbox
driver.find_element(By.CSS_SELECTOR, 'input#ap_password')


#'Re-enter password' textbox
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')


#'Create your Amazon account' button
driver.find_element(By.CSS_SELECTOR, '.a-button-input')


#'Conditions of Use' link
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")


#'Privacy Notice' link
driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")


#'Sign in' link
driver.find_element(By.XPATH, "//a[@class='a-link-emphasis']")
