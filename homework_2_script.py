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

driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//span[text()='Sign in']").click()
sleep(6)
driver.find_element(By.XPATH, "//span[contains(@class, 'styles__ListItemText-sc')]").click()
sleep(6)

expected_text_signin = 'Sign into your Target account'
actual_text_signin = driver.find_element(By.XPATH, "//h1[contains(@class,'styles__StyledHeading')]//span").text
assert expected_text_signin == actual_text_signin, f"Expected word {expected_text_signin} not in {actual_text_signin}"

driver.find_element(By.ID, 'login')

print("Test case passes")
driver.quit()
