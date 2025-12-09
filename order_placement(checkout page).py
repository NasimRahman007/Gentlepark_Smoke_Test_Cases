import time

import pytest
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


#Placing_order_as_registered_user_on_checkout_page:

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

driver.find_element(By.LINK_TEXT, "Shop").click()


wait_6 = WebDriverWait(driver, 15)
category_link = wait_6.until(expected_conditions.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Category']")))
category_link.click()

wait_7 = WebDriverWait(driver, 15)
subcategory_link = wait_7.until(expected_conditions.visibility_of_element_located((By.XPATH, "(//span[@class='text-nowrap typo-12mc text-dark uppercase'][normalize-space()='Polo Shirt Half'])[1]")))
subcategory_link.click()

wait_2 = WebDriverWait(driver, 15)
load_more_btn = (By.CSS_SELECTOR,"button[class='cursor-pointer bg-[#FFFFFF] !border !border-[#020617] px-[60px] py-4 text-dark typo-12sb transition-all duration-300 hover:bg-dark hover:text-white w-full sm:w-fit']")

while True:
    try:
        # wait until the button is clickable
        button = wait_2.until(expected_conditions.element_to_be_clickable(load_more_btn))
        button.click()
        print("Clicked 'Load More' button")
    except (TimeoutException, NoSuchElementException):
        print("No more 'Load More' button found. All products loaded.")
        break

time.sleep(3)
driver.find_element(By.XPATH, '//img[@alt="Steel Blue Zip Polo Shirt"]').click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[normalize-space()='XXL']").click()
driver.find_element(By.XPATH, "//div//div//div//div//div//div//div[3]//div[1]//button[2]").click()

wait_3 = WebDriverWait(driver, 15)
add_to_cart_btn = wait_3.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add To Cart']")))
add_to_cart_btn.click()

wait_4 = WebDriverWait(driver, 15)
continue_to_checkout_btn = wait_4.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[normalize-space()='continue to checkout']")))
continue_to_checkout_btn.click()

wait_5 = WebDriverWait(driver, 15)
continue_to_delivery_options_btn = wait_5.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Continue to Delivery Options']")))
continue_to_delivery_options_btn.click()

driver.find_element(By.XPATH, "//button[normalize-space()='Continue to Payment']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//label[@for='cash_on_delivery']").click()
time.sleep(2)

wait_8 = WebDriverWait(driver, 15)
place_order_btn = wait_8.until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[contains(@class,'hidden lg:block')]//button[normalize-space()='Place order']")))
place_order_btn.click()

print("Order has been placed successfully.")
