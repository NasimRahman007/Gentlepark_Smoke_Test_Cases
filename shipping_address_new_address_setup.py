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



#test_new_address_setup():

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

wait_3 = WebDriverWait(driver, 15)
add_new_address_button = wait_3.until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Add new address']")))
add_new_address_button.click()


driver.find_element(By.XPATH, "//input[@placeholder='Full Name*']").send_keys("Punki Kitty")

driver.find_element(By.XPATH, "//input[@placeholder='Address Line 1*']").send_keys("Kitty Street")



dropdown_1 = Select(driver.find_element(By.XPATH, "(//select[@aria-hidden='true'])[1]"))
dropdown_1.select_by_visible_text("Dhaka")

dropdown_2 = Select(driver.find_element(By.XPATH, "(//select[@aria-hidden='true'])[2]"))
dropdown_2.select_by_visible_text("Dhaka")
time.sleep(1)


driver.find_element(By.XPATH, "//input[@placeholder='Postal Code']").send_keys("1216")

driver.find_element(By.XPATH, "//input[@placeholder='Phone Number*']").send_keys("+8801966527205")

driver.find_element(By.XPATH, "//label[text()='Set as default shipping address']").click()

driver.find_element(By.XPATH, "(//button[text()='Add new shipping address'])[1]").click()
time.sleep(2)

driver.refresh()
