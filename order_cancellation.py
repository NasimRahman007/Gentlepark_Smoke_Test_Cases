import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest
from selenium.webdriver.common.keys import Keys


#test_order_cancellation_status():

options_chrome = Options()
options_chrome.add_experimental_option(name="detach",value=True)
service_obj = Service()
driver = webdriver.Chrome(service=service_obj, options=options_chrome)

driver.implicitly_wait(10)

# Navigate to the website
driver.get("https://gentle-park.hellonotionhive.com/")
driver.maximize_window()

# Accept cookies
wait_1 = WebDriverWait(driver, 15)
accept_all_btn = wait_1.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div/button[normalize-space()='Accept All']")))
accept_all_btn.click()

# Navigate to Sign In page
driver.find_element(By.LINK_TEXT, "SIGN IN").click()
time.sleep(2)

# Enter login credentials and sign in
driver.find_element(By.NAME, "email").send_keys("nasim@notionhive.com")
driver.find_element(By.NAME, "password").send_keys("Quantem007#")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
time.sleep(2)

# Navigate to "My Orders" page
wait_2 = WebDriverWait(driver, 15)
my_orders_link = wait_2.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[@class='hover:underline text-nowrap'][normalize-space()='My Orders']")))
my_orders_link.click()


# Open the details of the first order
wait_3 = WebDriverWait(driver, 15)
order_details_link = wait_3.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//a[@class='hover:underline uppercase w-fit typo-14m'][normalize-space()='Order Details'])[1]")))
order_details_link.click()


# Cancel the order
wait_4 = WebDriverWait(driver, 15)
cancel_order = wait_4.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Cancel Order']")))
cancel_order.click()

# Confirm cancellation
wait_5 = WebDriverWait(driver, 15)
confirm_cancel_order = wait_5.until(expected_conditions.element_to_be_clickable((By.XPATH, "(//button[@class='typo-14sbc flex justify-center items-center w-fit p-5 select-none text-white bg-dark/90 hover:bg-dark/90 disabled:text-[#7E8088] disabled:bg-[#E1E2E3] border border-transparent transition-colors duration-300 w-full'])[1]")))
confirm_cancel_order.click()

# Select reason for cancellation
wait_6 = WebDriverWait(driver, 15)
reason_for_cancellation = wait_6.until(expected_conditions.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Changed my mind']")))
reason_for_cancellation.click()

# Submit cancellation
wait_7 = WebDriverWait(driver, 15)
submit_cancellation = wait_7.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Confirm Cancellation']")))
submit_cancellation.click()
time.sleep(2)

# Navigate back to Orders page
wait_8 = WebDriverWait(driver, 15)
back_to_orders = wait_8.until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[text()='Back to Orders']")))
back_to_orders.click()
time.sleep(2)

# Verify the order status is updated to "Cancelled"
print("Order cancellation process completed")
