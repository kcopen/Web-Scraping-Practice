from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


driver = webdriver.Chrome()

driver.get("https://www.reddit.com")


driver.implicitly_wait(3)

search_bar = driver.find_element(by=By.ID, value="header-search-bar")

search_bar.send_keys("tacos")

search_value = search_bar.get_attribute('value')
assert search_value == "tacos"

search_button = driver.find_element(
    by=By.CLASS_NAME, value="_20OHBqoDD71_8fv7tuG6u6")


search_button.click()

driver.implicitly_wait(3)
search_results = driver.find_element(
    by=By.CLASS_NAME, value="SQnoC3ObvgnGjWt90zD9Z")

search_results.click()

sleep(10)

driver.quit()
