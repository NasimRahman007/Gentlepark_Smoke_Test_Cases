import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.common.keys import Keys


# test_read_addresses_from_address_book():
options_chrome = Options()
options_chrome.add_experimental_option(name="detach",value=True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=options_chrome)

driver.implicitly_wait(10)

driver.get("https://gentle-park.hellonotionhive.com/")
driver.maximize_window()


wait_1 = WebDriverWait(driver, 15)
accept_all_btn = wait_1.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/button[normalize-space()='Accept All']")))
accept_all_btn.click()


driver.find_element(By.LINK_TEXT, "SIGN IN").click()
time.sleep(2)


driver.find_element(By.NAME, "email").send_keys("nasim@notionhive.com")
driver.find_element(By.NAME, "password").send_keys("Quantem007#")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

wait_2 = WebDriverWait(driver, 15)
address_book_link = wait_2.until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[normalize-space()='Address Book']")))
address_book_link.click()
time.sleep(4)

wait_3 = WebDriverWait(driver, 15)
addresses = wait_3.until(expected_conditions.presence_of_all_elements_located((By.XPATH, "(//div[@class='flex items-start gap-2.5'])")))
addresses_in_browser = [address.text for address in addresses]
result = "\n\n".join(addresses_in_browser)
print(result)

print(f"Found {len(addresses)} addresses")
